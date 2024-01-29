## Master script for SDP analysis
#
# Author: Javier Ortiz-Tudela (Goethe Universitaet / University of Granada)
# January 2024

## ---------------------- Set up  ----------------------------
# Get the current working directory
root_dir <- getwd()

# Where is the data?
data_dir <- paste(root_dir, "../data", sep = "/")

## ------------------ Curate raw data files ----------------------
# Load function
source(paste(root_dir, "data_preprocessing/data_curation.R", sep = "/"))

# Loop through age groups
for (age_group in c("young_adults", "children", "older_adults")) {
  # Read participants ids from file
  which_subs <- read.csv(paste0(data_dir, "/raw/", age_group, "/ids.txt"),
    sep = ",", header = FALSE
  )$V1

  # Loop through participants
  for (c_sub in which_subs) {
    # Curate raw files
    data_curation(data_dir, c_sub, age_group)
  }

  ## ---------------------- Aggregate data (within groups) ------------
  # This function aggregates data within groups and does
  # some automatic coding of recall responses
  source(paste(root_dir, "data_preprocessing/agg_data_group.R", sep = "/"))
  agg_data_group(data_dir, which_subs, age_group)

  # Import coding. WARING! Only do this if the manual coding exists
  source(paste(root_dir, "data_preprocessing/import_coding.R", sep = "/"))
  import_coding(data_dir, age_group)
}

## ---------------------- Aggregate data (across groups) ------------
source(paste(root_dir, "data_preprocessing/agg_data_sample.R", sep = "/"))
age_group <- "full_sample"
agg_data_sample(data_dir)

# Print N by group
library(dplyr)
temp <- read.csv(paste(data_dir, "BIDS/full_sample/full-sample_task-sdp_beh.csv", sep = "/"), sep = ",", header = TRUE)
temp %>%
  group_by(group) %>%
  summarise(n = length(participant) / 80)

## ------------------------- ANALYSIS -------------------------------
## ---------------------- Encoding phase ----------------------------
# Stats
source(paste(root_dir, "analysis/encoding/stats_enc_acc.R", sep = "/"))
stats_enc_acc(root_dir)

# Plots
source(paste(root_dir, "analysis/encoding/plot_enc_acc.R", sep = "/"))
plot_enc_acc(data_dir)

## ------------ Retrieval phase. Overall performance ----------------
# Import all the retrieval scripts
ret_root_dir <- paste(root_dir, "retrieval", sep = "")
script_files <- list.files(ret_root_dir, pattern = "\\.R$", full.names = TRUE)
lapply(script_files, source)

# Stats
source(paste(root_dir, "retrieval/stats_story_rec.R", sep = ""))
stats_story_rec(data_dir)
source(paste(root_dir, "retrieval/stats_ending_type_mem.R", sep = ""))
stats_ending_type_mem(data_dir) # READY
source(paste(root_dir, "retrieval/stats_cued_recall.R", sep = ""))
stats_cued_recall(data_dir) # READY
source(paste(root_dir, "retrieval/stats_ending_rec.R", sep = ""))
stats_ending_rec(data_dir) # READY

# Plotting functions
source(paste(root_dir, "retrieval/plots_ending_type_mem.R", sep = ""))
plots_ending_type_mem(data_dir)

## ------------ Retrieval phase. By congruity ----------------
# Stats
source(paste(root_dir, "retrieval/mem_tasks.R", sep = ""))
mem_tasks(data_dir)

# Plots
source(paste(root_dir, "retrieval/plot_mem.R", sep = ""))
plot_mem(data_dir, "all")
source(paste(root_dir, "retrieval/plot_mem_cond.R", sep = ""))
plot_mem_cond(data_dir, which_subs, age_group)
