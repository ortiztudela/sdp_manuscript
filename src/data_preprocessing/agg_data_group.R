# Aggregate data for SASP study
# Author: Javier Ortiz-Tudela (Goethe Universitaet)
# October 2021

agg_data_group <- function(data_dir, which_subs, age_group) {
  ## ----------------------  Set up  ----------------------------

  # Load libraries
  library(dplyr)

  ## ----------------------  Load data -----------------------------
  # Where is the data?
  bids_dir <- paste(data_dir, "BIDS", age_group, sep = "/")

  # Pre-allocate
  merged_data <- data.frame(matrix(ncol = 0, nrow = 0))

  # Loop through participants
  for (c_sub in which_subs) {
    # Get subject code
    sub_code <- paste("sub-", sprintf("%02d", c_sub), sep = "")
    sub_dir <- paste(bids_dir, sub_code, sep = "/")

    # Load encoding data
    filename <- paste(sub_code, "_task-sdp_beh.csv", sep = "")

    # Read data from file
    sub_data <- read.csv(paste(sub_dir, filename, sep = "/"))

    # Store data
    merged_data <- rbind(merged_data, sub_data)
  }

  ## ----------------- Output recall responses for latter coding ---------
  # I will now code id_acc automatically. I've never done this before, but it feels like it should work and I will free a lot of time if it works decently (manually coding id_acc is not fun).
  library(stringr)

  # Make coding lower case
  merged_data$object <- as.character(merged_data$object)
  merged_data$central_recall_resp <- str_to_lower(merged_data$central_recall_resp)

  # Remove RETURN character from responses
  merged_data$central_recall_resp <- str_replace_all(merged_data$central_recall_resp, "\n", "")

  # Remove spaces from responses
  merged_data$central_recall_resp <- str_replace_all(merged_data$central_recall_resp, " ", "_")

  # Remove "a" at the start
  merged_data$central_recall_resp <- str_replace_all(merged_data$central_recall_resp, "a_", "")

  # Code for variations of frisbee
  merged_data$central_recall_resp <- str_replace_all(merged_data$central_recall_resp, "fresbee", "frisbee")
  merged_data$central_recall_resp <- str_replace_all(merged_data$central_recall_resp, "fresbi", "frisbee")
  merged_data$central_recall_resp <- str_replace_all(merged_data$central_recall_resp, "frisbi", "frisbee")

  # Fill empty responses
  merged_data$central_recall_resp[merged_data$central_recall_resp == ""] <- "empty"

  # Code acc.
  merged_data$id_acc <- str_detect(merged_data$object, merged_data$central_recall_resp) | str_detect(merged_data$central_recall_resp, merged_data$object)
  merged_data$id_acc[merged_data$id_acc == TRUE] <- 2

  ## ----------------------  Save merged data -------------------------
  # Output dir
  out_dir <- paste(bids_dir, "group_level", sep = "/")

  # Make group level dir
  if (!dir.exists(out_dir)) {
    dir.create(out_dir)
  }

  # Output names
  out_name <- paste("group_task-sdp_beh.csv", sep = "")

  # Write
  write.csv(merged_data, paste(out_dir, out_name, sep = "/"), row.names = FALSE)

  # I will output the incorrect ones to a new dataframe
  # for later manually coding. This new dataframe cannot contain
  # the condition info but only the  object ID and the object name.
  # It will also include the subject id and the trial number bcs
  # it will be combined later on with other participants into a
  # loooong dataframe (to optimize coding of similar answers. Trust me on this.)
  to_code <- merged_data %>%
    filter(id_acc == FALSE & central_recall_resp != "empty") %>%
    select(
      participant, trial_n_ret, comic_name,
      object, spec_obj_enc, central_recall_resp
    )

  # Output names
  out_name <- paste("group_task-sdp_desc-to-code_beh.csv", sep = "")

  # Write output file
  if (!file.exists(paste(out_dir, out_name, sep = "/"))) {
    write.csv(to_code, paste(out_dir, out_name, sep = "/"), row.names = FALSE)
  } else {
    print("Dir already exists! Watch out! Not creating the sheet to code.")
  }
}
