# Data curation for SDP study
# This script will curate the raw data files from the SDP study.
# It will create a BIDS folder with the data for each participant.
# It takes in the following arguments:
#   - data_dir: path to the data folder
#   - c_sub: participant id
#   - age_group: age group of the participant
#
#
# Author: Javier Ortiz-Tudela (Goethe Universitaet / University of Granada)
# October 2021
data_curation <- function(data_dir, c_sub, age_group) {
  ## ----------------------  Set up  ----------------------------
  # Load libraries
  library(dplyr)

  # Set up participant code
  sub_code <- paste("sub-", sprintf("%02d", c_sub), sep = "")

  ## ----------------------  Load data ----------------------------
  # Where is the data?
  raw_dir <- paste(data_dir, "raw", age_group, sep = "/")
  bids_dir <- paste(data_dir, "BIDS", age_group, sep = "/")

  # Make BIDS dir
  if (!dir.exists(bids_dir)) {
    dir.create(bids_dir)
  }

  # List data files
  file_pattern <- paste0("^", c_sub, "_sdp_ses-01_part-01_label-encoding*")
  filename <- list.files(path = raw_dir, pattern = file_pattern, full.names = T)

  # Read data from file
  raw <- read.csv(filename)

  ## ----------------------  Encoding phase ----------------------------
  # First, let's filter out practice and instructions rows and cols. 
  # I will also create a variable for trial number
  enc_data <- raw %>%
    filter(trials.ran == 1) %>%
    select(
      -starts_with("welcome"), -starts_with("pract"),
      -X.Scale, -Y.Scale, -date,
      -OS, -psychopyVersion, -inst_text,
      -expName, -frameRate
    ) %>%
    mutate(trial_n = trials.thisTrialN + 1) %>%
    select(-starts_with("trials."))

  # Rename accuracy var
  colnames(enc_data)[colnames(enc_data) == "target_resp.keys"] <- "enc_resp"
  colnames(enc_data)[colnames(enc_data) == "target_resp.corr"] <- "enc_acc"
  colnames(enc_data)[colnames(enc_data) == "target_resp.rt"] <- "enc_rt"

  # Remove enc_resp as we do not need it anymore
  enc_data <- enc_data %>%
    select(-enc_resp)

  # Output dir
  out_dir <- paste(bids_dir, sub_code, sep = "/")

  # Output name
  out_name <- paste(sub_code, "_task-sdp_desc-encoding_beh.csv", sep = "")

  # Make output dir
  if (!dir.exists(out_dir)) {
    dir.create(out_dir)
  } else {
    print("Dir already exists!")
  }

  ## ----------------------  Retrieval phase ----------------------------
  # Now I will do the same thing as before but with the retrieval phase.

  # List data files
  file_pattern <- paste0("^", c_sub, "_sdp_ses-01_part-01_label-retrieval*")
  filename <- list.files(path = raw_dir, pattern = file_pattern, full.names = T)

  # Read data from file
  raw <- read.csv(paste(filename, sep = ""))

  # First, let's filter out practice and instructions rows and cols. 
  # I will also create a variable for trial number
  ret_data <- raw %>%
    filter(trials.ran == 1) %>%
    select(
      -starts_with("welcome"), -starts_with("pract"),
      -X.Scale, -Y.Scale, -date,
      -OS, -psychopyVersion, -inst_text,
      -expName, -frameRate,
      -story_rec_resp.keys,
      -central_recall_resp.keys, -central_recall_resp.rt
    ) %>%
    mutate(trial_n = trials.thisTrialN + 1) %>%
    select(-starts_with("trials."))

  # Quick fix for random column
  if (c_sub == 249) {
    enc_data <- enc_data %>%
      select(-fbclid)
    ret_data <- ret_data %>%
      select(-fbclid)
  }

  # Rename accuracy vars
  colnames(ret_data)[colnames(ret_data) == "story_rec_resp.corr"] <- "story_rec_acc"
  colnames(ret_data)[colnames(ret_data) == "story_rec_resp.rt"] <- "story_rec_rt"
  colnames(ret_data)[colnames(ret_data) == "central_recall_textbox.text"] <- "central_recall_resp"
  colnames(ret_data)[colnames(ret_data) == "afc_resp.corr"] <- "afc_resp_acc"
  colnames(ret_data)[colnames(ret_data) == "ending_rec_resp_2.keys"] <- "ending_type_resp"
  colnames(ret_data)[colnames(ret_data) == "ending_rec_resp.keys"] <- "ending_type_resp"
  colnames(ret_data)[colnames(ret_data) == "ending_rec_resp_2.rt"] <- "ending_type_rt"
  colnames(ret_data)[colnames(ret_data) == "ending_rec_resp.rt"] <- "ending_type_rt"

  # Ending (mis)match does not have a correct response. Will do it here.
  ret_data$ending_type_corr_resp <- NA
  ret_data$ending_type_acc <- NA
  ret_data$ending_type_corr_resp[ret_data$OvsN == "old" & ret_data$congruency == "con"] <- "left"
  ret_data$ending_type_corr_resp[ret_data$OvsN == "old" & ret_data$congruency != "con"] <- "right"
  ret_data$ending_type_acc <- ret_data$ending_type_resp == ret_data$ending_type_corr_resp

  # Output name
  out_name <- paste(sub_code, "_task-sdp_desc-retrieval_beh.csv", sep = "")

  ## ----------------------  Merge phases ----------------------------
  merged_data <- merge(enc_data, ret_data, by = "comic_name", all.y = T, suffixes = c("_enc", "_ret"))

  # Clean up a little to remove duplicates
  merged_data <- merged_data %>%
    select(-c(
      "object_ret", "cong_code_ret", "congruency_ret",
      "relationship_ret", "participant_enc", "violation_ret",
      "context_ret", "schema_ret"
    ))

  # Rename some columns
  colnames(merged_data)[colnames(merged_data) == "object_enc"] <- "object"
  colnames(merged_data)[colnames(merged_data) == "cong_code_enc"] <- "cong_code"
  colnames(merged_data)[colnames(merged_data) == "congruency_enc"] <- "congruency"
  colnames(merged_data)[colnames(merged_data) == "relationship_enc"] <- "relationship"
  colnames(merged_data)[colnames(merged_data) == "participant_ret"] <- "participant"
  colnames(merged_data)[colnames(merged_data) == "violation_enc"] <- "violation"
  colnames(merged_data)[colnames(merged_data) == "context_enc"] <- "context"
  colnames(merged_data)[colnames(merged_data) == "schema_enc"] <- "schema"

  # Output name
  out_name <- paste(sub_code, "_task-sdp_beh.csv", sep = "")

  # Write
  write.csv(merged_data, paste(out_dir, out_name, sep = "/"), row.names = FALSE)
}
