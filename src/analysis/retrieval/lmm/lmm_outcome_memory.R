# Analysis of the outcome memory task in SDP
# Author: Javier Ortiz-Tudela (Goethe Universitaet / University of Granada)
# October 2021

lmm_outcome_memory <- function(data_dir) {
  ## ----------------------  Set up  ----------------------------
  # Load libraries
  library(dplyr)
  library(lme4)
  library(rstatix)

  ## ----------------------  Load data ----------------------------
  # Where is the data?
  bids_dir <- paste(data_dir, "BIDS/full_sample/", sep = "/")

  # List data files
  filename <- "full-sample_task-sdp_beh.csv"

  # Read data from file
  ret_data <- read.csv(paste(bids_dir, filename, sep = "/"))

  # Sort the levels
  ret_data <- ret_data %>%
    mutate(congruency = factor(congruency, levels = c("con", "neu", "inc")))
  ret_data <- ret_data %>%
    mutate(group = factor(group, levels = c("children", "YA", "OA")))

  # Filter out new items
  ret_data <- ret_data %>%
    filter(group == "YA", OvsN == "old")

  ## ------------------------------------------------------------------
  ## ---------------------- Model comparison --------------------------
  ## ------------------------------------------------------------------

  # Maximal model
  max_model <- glmer(
    ending_type_acc ~ congruency +
      (congruency | participant) +
      (congruency | comic_name),
    data = ret_data, family = binomial,
    control = glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000))
  )

  # Reduced model (-1)
  red_model_1a <- glmer(
    ending_type_acc ~ congruency +
      (1 | participant) +
      (congruency | comic_name),
    data = ret_data, family = binomial,
    control = glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000))
  )

  # Now we can compare the models.
  anova(max_model, red_model_1a)

  # As there is a significant decrease in fit, we keep individual variability
  # in our participants' reaction to the congruity manipulation
  # Let's check what happens with congruity by stimulus
  red_model_1b <- glmer(
    ending_type_acc ~ congruency +
      (congruency | participant) +
      (1 | comic_name),
    data = ret_data, family = binomial,
    control = glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000))
  )

  # Now we can compare the models.
  anova(max_model, red_model_1b)

  # As there is a significant decrease in fit, we keep individual variability
  # in our stimulus' reaction to the congruity manipulation.
  # We accept max_model
  # We can explore this model with "Anova" (capital A)
  Anova(max_model)
  summary(max_model)

  ## ------------------------------------------------------------------
  ## ------------------ Linear and quadratic test ---------------------
  ## ------------------------------------------------------------------

  # Define linear
  linear_comp <- c(-1, 0, 1)

  # Define quadratic
  quadratic_comp <- c(1, -2, 1)

  # Some R magic
  contrasts(ret_data$congruency) <- cbind(linear_comp, quadratic_comp)

  # refit the model
  max_model_contr <- glmer(
    ending_type_acc ~ congruency +
      (congruency | participant) +
      (congruency | comic_name),
    data = ret_data, family = binomial,
    control = glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000))
  )

  summary(max_model_contr)

  # Linear component in YA. No quadratic.
}
