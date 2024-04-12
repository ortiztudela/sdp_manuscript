# Analysis of the outcome memory task in SDP
# Author: Javier Ortiz-Tudela (Goethe Universitaet / University of Granada)
# October 2021

anova_outcome_memory <- function(data_dir) {
  ## ----------------------  Set up  ----------------------------
  # Load libraries
  library(dplyr)
  library(BayesFactor)
  library(rstatix)
  library(effsize)

  ## ----------------------  Load data ----------------------------
  # Where is the data?
  bids_dir <- paste(data_dir, "BIDS/full_sample/", sep = "/")

  # List data files
  filename <- "full-sample_task-sdp_beh.csv"

  # Read data from file
  ret_data <- read.csv(paste(bids_dir, filename, sep = "/"))

  ## ------------------------------------------------------------------
  ## ------------------- Overall Outcome memory -----------------------
  ## ------------------------------------------------------------------

  # Aggregate
  agg_data <- ret_data %>%
    filter(OvsN == "old") %>%
    group_by(group, participant) %>%
    summarise(av_acc = mean(ending_type_acc))

  # Reordering group factor levels
  agg_data$group <- factor(agg_data$group,
    levels = c("children", "YA", "OA")
  )

  # Perform a t-test for each group against chance level (0.5)
  groups <- unique(agg_data$group)
  t_test_results <- lapply(groups, function(g) {
    group_data <- filter(agg_data, group == g)
    t.test(group_data$av_acc, mu = 0.5)
  })

  # Print results
  names(t_test_results) <- groups
  print(t_test_results)

  # Perform a Bayesian t-test for each group against chance level (0.5)
  groups <- unique(agg_data$group)
  t_test_results <- lapply(groups, function(g) {
    group_data <- filter(agg_data, group == g)
    ttestBF(group_data$av_acc, mu = 0.5)
  })

  # Print results
  names(t_test_results) <- groups
  print(t_test_results)

  # Compute Cohen's d for each group
  cohen_d_results <- lapply(groups, function(g) {
    group_data <- filter(agg_data, group == g)
    cohens_d(data = group_data, av_acc ~ 1, mu = 0.5, paired = FALSE)
  })

  # Print results
  names(cohen_d_results) <- groups
  print(cohen_d_results)
  

  ## ------------------------------------------------------------------
  ## --------------- Outcome memory memory by congruency --------------
  ## ------------------------------------------------------------------
  # Since there's only above chance performance in young adults,
  # we will compute the ANOVA only in this group
  agg_data <- ret_data %>%
    filter(OvsN == "old", group == "YA") %>%
    group_by(participant, congruency) %>%
    summarise(av_acc = mean(ending_type_acc))

  # Fix R stuff
  agg_data <- agg_data %>% ungroup()
  agg_data$participant <- as.factor(agg_data$participant)
  agg_data$congruency <- as.factor(agg_data$congruency)

  # Run anova
  res.aov <- anova_test(
    data = agg_data,
    dv = av_acc, wid = participant, within = congruency
  )
  results <- get_anova_table(res.aov)
  print("Results ANOVA")
  print(results)

  # Pair-wise comparisons
  pwc <- agg_data %>%
    pairwise_t_test(
      av_acc ~ congruency,
      paired = TRUE,
      p.adjust.method = "bonferroni"
    )
  print(pwc)

  print(t.test(agg_data$av_acc[agg_data$congruency == "inc"], agg_data$av_acc[agg_data$congruency == "con"], paired = TRUE))
  print(t.test(agg_data$av_acc[agg_data$congruency == "inc"], agg_data$av_acc[agg_data$congruency == "neu"], paired = TRUE))
  print(t.test(agg_data$av_acc[agg_data$congruency == "neu"], agg_data$av_acc[agg_data$congruency == "con"], paired = TRUE))
  print(cohens_d(data = agg_data, av_acc ~ congruency, paired = TRUE))

  ## ------------------------------------------------------------------
  ## --------- Outcome memory memory by congruency (revision) ---------
  ## ------------------------------------------------------------------
  # In response to reviewer #1, we will compute the ANOVA in all groups
  agg_data <- ret_data %>%
    filter(OvsN == "old") %>%
    group_by(group, participant, congruency) %>%
    summarise(av_acc = mean(ending_type_acc))

  # Fix R stuff
  agg_data <- agg_data %>% ungroup()
  agg_data$participant <- as.factor(agg_data$participant)
  agg_data$congruency <- as.factor(agg_data$congruency)
  agg_data$group <- factor(agg_data$group,
    levels = c("children", "YA", "OA")
  )

  # Run anova
  res.aov <- anova_test(
    data = agg_data,
    dv = av_acc, wid = participant, within = congruency, between = group)

  results <- get_anova_table(res.aov)
  print("Results ANOVA")
  print(results)

}
