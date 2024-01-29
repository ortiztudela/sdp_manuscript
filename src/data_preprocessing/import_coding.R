# Aggregate data for SASP study
# Author: Javier Ortiz-Tudela (Goethe Universitaet)
# October 2021

import_coding <- function(data_dir, age_group) {
  ## ----------------------  Set up  ----------------------------

  # Load libraries
  library(dplyr)

  ## ----------------------  Load data ----------------------------
  # Where is the data?
  bids_dir <- paste(data_dir, "BIDS", age_group, "group_level", sep = "/")

  # List data files
  filename <- "group_task-sdp_beh.csv"

  # Read data from file
  ret_data <- read.csv(paste(bids_dir, filename, sep = "/"))

  ## ----------------------  Load coding ----------------------------

  # List data files
  filename <- "group_task-sdp_desc-coded.csv"

  # Read data from file
  coding <- read.csv(paste(bids_dir, filename, sep = "/"), sep = ",")

  ## ----------------------  Merge -------------------------
  # Merge manual and automatic coding
  merged_data <- merge(ret_data, coding, by = c("participant", "comic_name"), all.x = T, suffixes = c("_ret", "_coding"))
  colnames(merged_data)[colnames(merged_data) == "coding"] <- "central_recall_coding"

  # I will output the ones that are still not coded to a new dataframe for later manually coding. This new dataframe cannot contain the condition info but only the  object ID and the object name. It will also include the subject id and the trial number bcs it will be combined later on with other participants into a loooong dataframe (to optimize coding of similar answers. Trust me on this.)
  to_code <- merged_data %>%
    filter(id_acc == FALSE, is.na(central_recall_coding), OvsN == "old", central_recall_resp_ret != "empty") %>%
    select(participant, trial_n_ret_ret, comic_name, object_ret, spec_obj_enc_ret, central_recall_resp_ret)

  # Re-code variables
  colnames(to_code)[colnames(to_code) == "trial_n_ret_ret"] <- "trial_n_ret"
  colnames(to_code)[colnames(to_code) == "object_ret"] <- "object"
  colnames(to_code)[colnames(to_code) == "spec_obj_enc_ret"] <- "spec_obj_enc"
  colnames(to_code)[colnames(to_code) == "central_recall_resp_ret"] <- "central_recall_resp"

  # Output names
  out_name <- paste("group_task-sdp_desc-left-to-code_beh.csv", sep = "") # If everything goes well, this should be blank

  # Write
  write.csv(to_code, paste(bids_dir, out_name, sep = "/"), row.names = FALSE)

  # Clean up
  merged_data$coding[is.na(merged_data$central_recall_coding)] <- 0
  merged_data$central_recall_coding[is.na(merged_data$central_recall_coding)] <- 0
  merged_data$central_recall_coding <- as.numeric(merged_data$central_recall_coding)
  merged_data$coding_auto_manual[merged_data$OvsN == "old"] <- merged_data$central_recall_coding[merged_data$OvsN == "old"] + merged_data$id_acc[merged_data$OvsN == "old"]
  merged_data$item_recall_acc[merged_data$central_recall_coding == 3] <- 1
  merged_data$item_recall_acc[merged_data$central_recall_coding == 2] <- 0
  merged_data$item_recall_acc[merged_data$central_recall_coding == 1] <- 0
  merged_data$item_recall_acc[merged_data$central_recall_coding == 0] <- 0
  merged_data$obj_type_recall_acc[merged_data$central_recall_coding == 3] <- 1
  merged_data$obj_type_recall_acc[merged_data$central_recall_coding == 2] <- 1
  merged_data$obj_type_recall_acc[merged_data$central_recall_coding == 1] <- 0
  merged_data$obj_type_recall_acc[merged_data$central_recall_coding == 0] <- 0
  merged_data$action_recall_acc[merged_data$central_recall_coding == 3] <- 1
  merged_data$action_recall_acc[merged_data$central_recall_coding == 2] <- 1
  merged_data$action_recall_acc[merged_data$central_recall_coding == 1] <- 1
  merged_data$action_recall_acc[merged_data$central_recall_coding == 0] <- 0

  # Output names
  out_name <- paste("group_task-sdp_beh.csv", sep = "")

  # Write
  write.csv(merged_data, paste(bids_dir, out_name, sep = "/"), row.names = FALSE)
}
