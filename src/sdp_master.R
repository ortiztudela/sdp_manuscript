## Master script for SDP analysis
#
# Author: Javier Ortiz-Tudela (Goethe Universitaet / University of Granada)
# January 2024

## ---------------------- Set up  ----------------------------
# Get the current working directory
root_dir <- getwd()

# Where is the data?
data_dir <- paste(root_dir, "../data", sep = "/")

## --------------------- PREPROCESSING ---------------------------
# ------------------ Curate raw data files ----------------------
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

  # ---------------------- Aggregate data (within groups) ------------
  # This function aggregates data within groups and does
  # some automatic coding of recall responses
  source(paste(root_dir, "data_preprocessing/agg_data_group.R", sep = "/"))
  agg_data_group(data_dir, which_subs, age_group)

  # Import coding. WARING! Only do this if the manual coding exists
  source(paste(root_dir, "data_preprocessing/import_coding.R", sep = "/"))
  import_coding(data_dir, age_group)
}

# ---------------------- Aggregate data (across groups) ------------
source(paste(root_dir, "data_preprocessing/agg_data_sample.R", sep = "/"))
age_group <- "full_sample"
agg_data_sample(data_dir)

# Print N by group
library(dplyr)
temp <- read.csv(paste(data_dir, "BIDS/full_sample/full-sample_task-sdp_beh.csv", sep = "/"), sep = ",", header = TRUE)
temp %>%
  group_by(group) %>%
  summarise(n = length(participant) / 80)

## --------------------- ANALYSIS (ANOVA) ---------------------------
# ----------------------- Encoding phase ----------------------------

# Stats
source(paste(root_dir, "analysis/encoding/stats_enc_acc.R", sep = "/"))
stats_enc_acc(root_dir)

# ----------------------- Retrieval phase  --------------------------

# Cue recognition
source(paste(root_dir, "analysis/retrieval/anova/anova_cue_recog.R", sep = "/"))
anova_cue_recog(data_dir)

# Object recall
source(paste(root_dir, "analysis/retrieval/anova/anova_object_recall.R", sep = "/"))
anova_object_recall(data_dir)

# Outcome memory
source(paste(root_dir, "analysis/retrieval/anova/anova_outcome_memory.R", sep = "/"))
anova_outcome_memory(data_dir)

# Ending recog
source(paste(root_dir, "analysis/retrieval/anova/anova_ending_recog.R", sep = "/"))
anova_ending_recog(data_dir)

## --------------------- ANALYSIS (LMM) -----------------------------
# ---------------------- Retrieval phase  ---------------------------
# Warning! This is a very slow process. It may take several hours to run.
# Cue recognition
source(paste(root_dir, "analysis/retrieval/lmm/lmm_cue_recog.R", sep = "/"))
lmm_cue_recog(data_dir)

# Object recall
source(paste(root_dir, "analysis/retrieval/lmm/lmm_object_recall.R", sep = "/"))
lmm_object_recall(data_dir)

# Outcome memory
source(paste(root_dir, "analysis/retrieval/lmm/lmm_outcome_memory.R", sep = "/"))
lmm_outcome_memory(data_dir)

# Ending recog
source(paste(root_dir, "analysis/retrieval/lmm/lmm_ending_recog.R", sep = "/"))
lmm_ending_recog(data_dir)

## ------------------------ FIGURES --------------------------------
# ----------------------- Encoding phase ----------------------------

# Figures
source(paste(root_dir, "analysis/encoding/plot_enc_acc.R", sep = "/"))
plot_enc_acc(data_dir)

# ---------------------- Retrieval phase  ---------------------------
# Cue recognition
source(paste(root_dir, "visualization/cue-recog_create-plots.R", sep = "/"))

# Object recall
source(paste(root_dir, "visualization/object-recall_create-plots.R", sep = "/"))

# Outcome memory
source(paste(root_dir, "visualization/outcome-memory_create-plots.R", sep = "/"))

# Ending recog
source(paste(root_dir, "visualization/ending-recog_create-plots.R", sep = "/"))

# Polynomials
source(paste(root_dir, "visualization/polynomials_create-plots.R", sep = "/"))