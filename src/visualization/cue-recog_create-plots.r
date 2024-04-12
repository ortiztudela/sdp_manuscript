# Figures of the cue recognition task in SDP
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
fig_dir <- paste(main_dir, "figures/retrieval/", sep = "/")

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
  story_rec_acc ~ congruency * group +
    (1 | participant) +
    (1 | comic_name),
  data = old_data, family = binomial,
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
    av_story_rec = mean(story_rec_acc)
  )

# Get FAs
fa_data <- ret_data %>%
  filter(OvsN == "new") %>%
  group_by(group, participant) %>%
  summarise(ov_fas = 1 - mean(story_rec_acc))

# Compute Hits-FAs
agg_data$hits_minus_fas <- NA
for (c_sub in fa_data$participant) {
  temp <- agg_data %>%
    filter(participant == c_sub) %>%
    group_by(congruency) %>%
    mutate(hits_minus_fas = av_story_rec - fa_data$ov_fas[fa_data$participant == c_sub])

  agg_data$hits_minus_fas[agg_data$participant == c_sub] <- temp$hits_minus_fas
}

# Get FAs at the group level
fa_group_data <- fa_data %>%
  group_by(group) %>%
  summarise(ov_fas = mean(ov_fas)) %>%
  mutate(group = factor(group, levels = c("children", "YA", "OA")))

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

# Calculate the adjusted intercept for each group based on model coefficients
intercepts <- calculate_intercepts(red_model_2, fa_group_data)

# Get polynomial coefficients from the model
coefficients <- list(
  "children" = list(intercept = intercepts$children, linear = 0.143, quadratic = 0.085),
  "YA" = list(intercept = intercepts$YA, linear = 0.180, quadratic = 0.088),
  "OA" = list(intercept = intercepts$OA, linear = 0.046, quadratic = 0.032)
)

# Using the function to create
final_plot <- spag_plot(
  agg_data = agg_data,
  y_var = agg_data$hits_minus_fas,
  chance_level = 0,
  y_lab = "Hits - False Alarms",
  title = "Cue recognition"
)

# Saving the final plot
plot_filename <- paste(fig_dir, "cue-recog_lmm.pdf", sep = "/")
ggsave(plot_filename, final_plot)
