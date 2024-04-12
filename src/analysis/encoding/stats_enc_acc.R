# Analysis of the encoding task in SDP
# Author: Javier Ortiz-Tudela (Goethe Universitaet / University of Granada)
# October 2021

stats_enc_acc <- function(root_dir) {
  ## ----------------------  Set up  ----------------------------
  # Load libraries
  library(dplyr)
  library(rstatix)

  ## ----------------------  Load data ----------------------------
  # Where is the data?
  bids_dir <- paste(root_dir, "../data/BIDS/full_sample/", sep = "/")

  # List data files
  filename <- "full-sample_task-sdp_beh.csv"

  # Read data from file
  enc_data <- read.csv(paste(bids_dir, filename, sep = "/"))

  ## ------------------------------------------------------------------
  ## ------------------------ Encoding accuracy -----------------------
  ## ------------------------------------------------------------------
  agg_data_ov <- enc_data %>%
    filter(OvsN == "old") %>%
    group_by(group) %>%
    summarise(
      av_acc = mean(enc_acc),
      sd_acc = sd(enc_acc)
    )

  # Reordering group factor levels
  agg_data_ov$group <- factor(agg_data_ov$group,
    levels = c("children", "YA", "OA")
  )

  # Print means and standard deviations
  print("Overall encoding performance by group")
  print(agg_data_ov)

  ### 3-way ANOVA ###
  # Aggregated data by participants
  agg_data <- enc_data %>%
    filter(OvsN == "old") %>%
    group_by(group, participant) %>%
    summarise(av_acc = mean(enc_acc))

  # Fix R stuff
  agg_data <- agg_data %>% ungroup()
  agg_data$participant <- as.factor(agg_data$participant)
  agg_data$group <- as.factor(agg_data$group)

  # Prepare data
  prepared_data <- agg_data %>%
    select(group, participant, av_acc)
    
  # Between-subjects comparison using Kruskal-Wallis test
  res_between <- kruskal_test(av_acc ~ group, data = prepared_data)

  # Pairwise comparisons between groups using Mann-Whitney U test with Bonferroni correction
  pwc_nonparam <- prepared_data %>%
    pairwise_wilcox_test(
      av_acc ~ group,
      p.adjust.method = "bonferroni"
    )

  # Display results
  print(res_between)
  print(pwc_nonparam)
}
