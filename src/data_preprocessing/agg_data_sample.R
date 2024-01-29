# Aggregate data across age groups for SASP study
# Author: Javier Ortiz-Tudela (Goethe Universitaet / University of Granada)
# January 2024
# Description: This function aggregates data samples from a specified directory.
# It saves the aggregated data in the specified directory.
# Parameters:
#   - data_dir: The directory where the data samples are located.
# Returns: None.

agg_data_sample <- function(data_dir) {
  ## ----------------------  Set up  ----------------------------
  # Load libraries
  library(dplyr)

  ## ----------------------  Load data ---------------
  # Group file name (after coding)
  filename <- "group_task-sdp_beh.csv"

  # Read data from file
  children_data <- read.csv(paste(data_dir, "BIDS/children/group_level", filename, sep = "/"), sep = ",", header = TRUE)
  ya_data <- read.csv(paste(data_dir, "BIDS/young_adults/group_level", filename, sep = "/"), sep = ",", header = TRUE)
  oa_data <- read.csv(paste(data_dir, "BIDS/older_adults/group_level", filename, sep = "/"), sep = ",", header = TRUE)

  # Add group identifier
  children_data$group <- rep("children", length(children_data$participant))
  ya_data$group <- rep("YA", length(ya_data$participant))
  oa_data$group <- rep("OA", length(oa_data$participant))

  # Merge groups
  merged_data <- rbind(children_data, ya_data, oa_data)

  ## ----------------------  Save merged data -------------------------
  # Output dir
  out_dir <- paste(data_dir, "BIDS/full_sample/", sep = "/")

  # Make full sample dir
  if (!dir.exists(out_dir)) {
    dir.create(out_dir)
  }

  # Output names
  out_name <- paste("full-sample_task-sdp_beh.csv", sep = "")

  # Write
  write.csv(merged_data, paste(out_dir, out_name, sep = "/"), row.names = FALSE)
}
