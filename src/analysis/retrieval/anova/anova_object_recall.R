# Analysis of the object recall task in SDP
# Author: Javier Ortiz-Tudela (Goethe Universitaet / University of Granada)
# October 2021

anova_object_recall <- function(data_dir) {
  ## ----------------------  Set up  ----------------------------
  # Load libraries
  library(dplyr)

  ## ----------------------  Load data ----------------------------
  # Where is the data?
  bids_dir <- paste(data_dir, "BIDS/full_sample/", sep = "/")

  # List data files
  filename <- "full-sample_task-sdp_beh.csv"

  # Read data from file
  ret_data <- read.csv(paste(bids_dir, filename, sep = "/"))

  # Reordering group factor levels
  ret_data$group <- factor(ret_data$group,
    levels = c("children", "YA", "OA")
  )

  # How many Ps?
  which_subs <- unique(ret_data$participant)

  ## ------------------------------------------------------------------
  ## --------------------------- Cued recall  -------------------------
  ## ------------------------------------------------------------------
  # Aggregate
  agg_data <- ret_data %>%
    filter(OvsN == "old") %>%
    filter(participant %in% which_subs) %>%
    group_by(group, participant) %>%
    summarise(
      n_rec_action = sum(action_recall_acc),
      n_rec_obj_type = sum(obj_type_recall_acc),
      n_rec_item = sum(item_recall_acc),
      recall_cont = mean(central_recall_coding)
    )

  ## ------------------------------------------------------------------
  ## --------- Cued recall by congruency ------------
  ## ------------------------------------------------------------------
  # Aggregate
  agg_data <- ret_data %>%
    filter(OvsN == "old") %>%
    group_by(group, participant, congruency) %>%
    summarise(recall_cont = mean(central_recall_coding))

  # Fix R stuff
  agg_data <- agg_data %>% ungroup()
  agg_data$participant <- as.factor(agg_data$participant)
  agg_data$congruency <- as.factor(agg_data$congruency)

  # Run 3x3 anova
  res.aov <- anova_test(
    data = agg_data,
    dv = recall_cont, wid = participant, within = congruency, between = group
  )
  results <- get_anova_table(res.aov)
  print("Results ANOVA")
  print(results)
}
