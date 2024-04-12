# Analysis of the object recall task in SDP
# Author: Javier Ortiz-Tudela (Goethe Universitaet / University of Granada)
# October 2021

object_recall <- function(data_dir) {
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
    filter(OvsN == "old")

  ## ------------------------------------------------------------------
  ## ---------------------- Model comparison --------------------------
  ## ------------------------------------------------------------------

  # Maximal model
  max_model <- lmer(
    central_recall_coding ~ congruency * group +
      (congruency | participant) +
      (congruency | comic_name),
    data = ret_data
  )

  # Reduced model (-1)
  red_model_1a <- lmer(
    central_recall_coding ~ congruency * group +
      (congruency | participant) +
      (1 | comic_name),
    data = ret_data
  )

  # Now we can compare the models.
  anova(max_model, red_model_1a)

  # As there is no significant decrease in fit, we discard individual variability
  # in our stimuli's reaction to the congruity manipulation
  # Let's check what happens with congruity by subject.
  red_model_1b <- lmer(
    central_recall_coding ~ congruency * group +
      (1 | participant) +
      (congruency | comic_name),
    data = ret_data
  )

  # Now we can compare the models.
  anova(max_model, red_model_1b)

  # As there is no significant decrease in fit, we discard individual variability
  # in our participant's reaction to the congruity manipulation. We need a model without both random slopes
  red_model_1 <- lmer(
    central_recall_coding ~ congruency * group +
      (1 | participant) +
      (1 | comic_name),
    data = ret_data
  )
  # Let's test the intercept for participants
  red_model_2a <- lmer(
    central_recall_coding ~ congruency * group +
      (1 | comic_name),
    data = ret_data
  )

  anova(red_model_1, red_model_2a)
  # As there is a significant decrease in fit, we keep participants' intercept
  # Let's test the intercept for stimuli
  red_model_2b <- lmer(
    central_recall_coding ~ congruency * group +
      (1 | participant),
    data = ret_data
  )

  anova(red_model_1, red_model_2b)
  # As there is a significant decrease in fit, we keep stimuli's intercept
  # As there's nothing else to reduce, we keep red_model_1
  # We can explore this model with "Anova" (capital A)
  Anova(red_model_1)
  summary(red_model_1)

}
