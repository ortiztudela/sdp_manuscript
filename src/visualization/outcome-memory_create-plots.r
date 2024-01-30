# Figures of the outcome memory task in SDP
# Author: Javier Ortiz-Tudela (Goethe Universitaet / University of Granada)
# October 2021
# Description:

## ----------------------  Set up  ----------------------------
# Load libraries
library(dplyr)
library(lme4)

# Set working directory
main_dir <- paste(getwd(), "../", sep = "/")

# Where is the data?
data_dir <- paste(main_dir, "data/BIDS/full_sample/", sep = "/")

# Where do you want the plots?
fig_dir <- paste(main_dir, "results/figures/retrieval/", sep = "/")

# Create the directory if it doesn't exist
if (!dir.exists(fig_dir)) {
  dir.create(fig_dir)
}

## ----------------------  Load data ----------------------------

# List data files
filename <- "full-sample_task-sdp_beh.csv"

# Read data from file
ret_data <- read.csv(paste(data_dir, filename, sep = "/"))

# Convert group and congruency to factor
ret_data$group <- factor(ret_data$group)
ret_data$congruency <- factor(ret_data$congruency)

# Filter data to old items only
old_data <- ret_data %>%
  filter(OvsN == "old")

## ------------------------------------------------------------------
## -----------  Fit the model to trial level data -------------------
## ------------------------------------------------------------------

# Fit the model. This is the winning model from the model comparison
red_model_2 <- glmer(
  ending_type_acc ~ congruency +
    (congruency | participant) +
    (congruency | comic_name),
  data = ret_data, family = binomial,
  control = glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000))
)


## ------------------------------------------------------------------
## --------------------- Aggregate and wrangle data -----------------
## ------------------------------------------------------------------

# Aggregate data
agg_data <- ret_data %>%
  filter(OvsN == "old") %>%
  group_by(group, participant, congruency) %>%
  summarise(
    av_outcome_mem = mean(ending_type_acc)
  )

#  Reorder group and congruency factor levels
agg_data <- agg_data %>%
  mutate(
    group = factor(group, levels = c("children", "YA", "OA")),
    congruency = factor(congruency, levels = c("con", "neu", "inc"))
  )

## ------------------------------------------------------------------
## --------------------- Create plots -------------------------------
## ------------------------------------------------------------------

# Load custom plotting functions
source(paste(main_dir, "src/_custom_functions/plotting-functions.R", sep = ""))

# Using the function to create
final_plot <- spag_plot(
  agg_data = agg_data,
  y_var = agg_data$av_outcome_mem,
  chance_level = 0.5,
  y_lab = "Average accuracy",
  title = "C. Outcome memory",
  y_lim = c(0, 1)
)

# Saving the final plot
plot_filename <- paste(fig_dir, "outcome-mem_lmm.pdf", sep = "/")
ggsave(plot_filename, final_plot)
