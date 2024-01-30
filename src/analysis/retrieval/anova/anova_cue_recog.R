# Analysis of the cue recognition task in SDP
# Author: Javier Ortiz-Tudela (Goethe Universitaet / University of Granada)
# October 2021

anova_cue_recog <- function(data_dir) {
  ## ----------------------  Set up  ----------------------------
  # Load libraries
  library(dplyr)
  library(psycho)
  library(BayesFactor)
  library(rstatix)

  ## ----------------------  Load data ----------------------------
  # Where is the data?
  bids_dir <- paste(data_dir, "BIDS/full_sample/", sep = "/")

  # List data files
  filename <- "full-sample_task-sdp_beh.csv"

  # Read data from file
  ret_data <- read.csv(paste(bids_dir, filename, sep = "/"))

  # How many Ps?
  which_subs <- unique(ret_data$participant)
  n <- length(which_subs)

  ## ------------------------------------------------------------------
  ## ---------------- Overall Cue recognition -------------------------
  ## ------------------------------------------------------------------
  # Init
  sdt_out <- data.frame(
    participant = rep(9999, n), dprime = rep(9999, n),
    beta = rep(9999, n), group = NA
  )

  # Get SDT numbers for this participant
  for (c_sub in 1:n) {
    # Get number of responses of each type
    sdt_nbrs <- ret_data %>%
      filter(participant == which_subs[c_sub]) %>%
      group_by(participant, story_rec_acc) %>%
      count(OvsN)

    # Ugly fix for participants with 0 FAs. Should just pre-allocate
    ps_without_fas <- c(223, 314, 311, 319, 320, 326, 339, 343, 344, 345, 415)
    if (which_subs[c_sub] %in% ps_without_fas) {
      fa_fix <- data.frame(
        participant = which_subs[c_sub],
        story_rec_acc = 0, OvsN = "new", n = 0
      )
      sdt_nbrs[nrow(sdt_nbrs) + 1, ] <- fa_fix
    }

    # Re-arrange them
    n_hit <- sdt_nbrs$n[sdt_nbrs$OvsN == "old" & sdt_nbrs$story_rec_acc == 1]
    n_miss <- sdt_nbrs$n[sdt_nbrs$OvsN == "old" & sdt_nbrs$story_rec_acc == 0]
    n_fa <- sdt_nbrs$n[sdt_nbrs$OvsN == "new" & sdt_nbrs$story_rec_acc == 0]
    n_cr <- sdt_nbrs$n[sdt_nbrs$OvsN == "new" & sdt_nbrs$story_rec_acc == 1]

    # Compute dprime
    temp <- dprime(n_hit, n_miss, n_fa, n_cr)

    # Store it
    sdt_out$participant[c_sub] <- which_subs[c_sub]
    sdt_out$hit[c_sub] <- n_hit / (n_hit + n_miss)
    sdt_out$fa[c_sub] <- n_fa / (n_fa + n_cr)
    sdt_out$dprime[c_sub] <- temp$dprime
    sdt_out$beta[c_sub] <- temp$beta
    sdt_out$group[c_sub] <- unique(ret_data$group[ret_data$participant == which_subs[c_sub]])
  }

  # Echo to terminal
  message("Overall dprime: ")
  print(sdt_out %>%
          group_by(group) %>%
          summarise(av_dprime = mean(dprime)))

  # Perform an overall t-test on dprime against 0
  print(t.test(sdt_out$dprime, mu = 0))

  # Perform a Bayesian t-test on dprime against 0
  print(ttestBF(sdt_out$dprime, mu = 0))

  # Perform a t-test on dprime for each group against 0
  groups <- unique(sdt_out$group)
  t_test_results <- lapply(groups, function(g) {
    group_data <- filter(sdt_out, group == g)
    t.test(group_data$dprime, mu = 0)
  })

  # Print results
  names(t_test_results) <- groups
  print(t_test_results)

  ## ------------------------------------------------------------------
  ## ----------------- Cue recognition by congruency ------------------
  ## ------------------------------------------------------------------
  # Aggregate
  agg_data <- ret_data %>%
    filter(OvsN == "old") %>%
    group_by(group, participant, congruency) %>%
    summarise(av_acc = mean(story_rec_acc))

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
    print(cohens_d(
      data = single_group_data,
      av_acc ~ congruency, paired = TRUE
    ))
  }
  one_way_and_pair(agg_data, "children")
  one_way_and_pair(agg_data, "YA")
  one_way_and_pair(agg_data, "OA")
}
