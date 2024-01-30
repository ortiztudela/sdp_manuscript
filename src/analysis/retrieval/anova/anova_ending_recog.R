# Analysis of the memory tasks in SDP
# Author: Javier Ortiz-Tudela (Goethe Universitaet)
# October 2021

anova_ending_recog <- function(data_dir) {
  ## ----------------------  Set up  ----------------------------
  # Load libraries
  library(dplyr)
  library(rstatix)

  ## ----------------------  Load data ----------------------------
  # Where is the data?
  bids_dir <- paste(data_dir, "bids/full_sample/", sep = "/")

  # List data files
  filename <- "full-sample_task-sdp_beh.csv"

  # Read data from file
  ret_data <- read.csv(paste(bids_dir, filename, sep = "/"))

  # Reordering group factor levels
  ret_data$group <- factor(ret_data$group,
    levels = c("children", "YA", "OA")
  )

  ## ------------------------------------------------------------------
  ## ----------------Ending recognition (3AFC) ------------------------
  ## ------------------------------------------------------------------
  # Aggregate
  agg_data <- ret_data %>%
    filter(OvsN == "old") %>%
    group_by(group, participant) %>%
    summarise(av_rec = mean(afc_resp_acc))

  # Reordering group factor levels
  agg_data$group <- factor(agg_data$group,
    levels = c("children", "YA", "OA")
  )

  # Perform a t-test for each group against chance level (0.5)
  groups <- unique(agg_data$group)
  t_test_results <- lapply(groups, function(g) {
    group_data <- filter(agg_data, group == g)

    # Perform t-test
    t_test <- t.test(group_data$av_rec, mu = 0.33)

    # Compute Cohen's d
    mean_diff <- mean(group_data$av_rec) - 0.33
    sd_pooled <- sqrt(var(group_data$av_rec))
    cohen_d <- mean_diff / sd_pooled

    # Return both t-test result and Cohen's d
    list(t_test = t_test, cohen_d = cohen_d)
  })

  # Print results
  names(t_test_results) <- groups
  print(t_test_results)
  ## ------------------------------------------------------------------
  ## --------------- Ending recognition by congruency -----------------
  ## ------------------------------------------------------------------
  # Aggregate
  agg_data <- ret_data %>%
    filter(OvsN == "old") %>%
    group_by(group, participant, congruency) %>%
    summarise(av_acc = mean(afc_resp_acc))

  # Fix R stuff
  agg_data <- agg_data %>% ungroup()
  agg_data$participant <- as.factor(agg_data$participant)
  agg_data$congruency <- as.factor(agg_data$congruency)

  # Run 3x3 anova
  res_aov <- anova_test(
    data = agg_data,
    dv = av_acc, wid = participant, within = congruency, between = group
  )
  results <- get_anova_table(res_aov)
  print("Results ANOVA")
  print(results)

  # Run one-way ANOVA (per group)
  one_way_and_pair <- function(df, group_name) {
    single_group_data <- df %>%
      filter(group == group_name)
    res_aov <- anova_test(
      data = single_group_data,
      dv = av_acc, wid = participant, within = congruency
    )
    results <- get_anova_table(res_aov)
    print(paste("Results ANOVA  (", group_name, ")", sep = ""))
    print(results)

    # Pair-wise comparisons
    pwc <- single_group_data %>%
      pairwise_t_test(
        av_acc ~ congruency,
        paired = TRUE,
        p.adjust.method = "holm"
      )
    print(pwc)
    print(cohens_d(data = single_group_data, av_acc ~ congruency, paired = TRUE))
  }
  print(one_way_and_pair(agg_data, "children"))
  print(one_way_and_pair(agg_data, "YA"))
  print(one_way_and_pair(agg_data, "OA"))
}
