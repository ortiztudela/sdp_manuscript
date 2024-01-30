# Analysis of the memory tasks in SDP
# Author: Javier Ortiz-Tudela (Goethe Universitaet)
# October 2021

lmm_ending_recog <- function(main_dir, which_subs) {
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
  max_model <- glmer(
    afc_resp_acc ~ congruency * group +
      (congruency | participant) +
      (congruency | comic_name),
    data = ret_data, family = binomial,
    control = glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000))
  )

  # Reduced model (-1)
  red_model_1a <- glmer(
    afc_resp_acc ~ congruency * group +
      (1 | participant) +
      (congruency | comic_name),
    data = ret_data, family = binomial,
    control = glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000))
  )

  # Now we can compare the models.
  anova(max_model, red_model_1a)

  # As there is a significant decrease in fit, we keep individual variability
  # in our participants' reaction to the congruity manipulation
  # Let's check what happens with congruity by stimuli
  red_model_1b <- glmer(
    afc_resp_acc ~ congruency * group +
      (congruency | participant) +
      (1 | comic_name),
    data = ret_data, family = binomial,
    control = glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000))
  )

  # Now we can compare the models.
  anova(max_model, red_model_1b)

  # As there is a significant decrease in fit, we keep individual variability
  # in our stimuli' reaction to the congruity manipulation
  # We accept the maximal model
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

  # Function to create models with different baseline levels and contrasts
  group_poly_test <- function(df, age_group, contrasts_to_run) {
    print(paste("####### Baseline level:", age_group, "######"))
    # Chose baseline level
    df$group <- relevel(df$group, ref = age_group)

    # Add contrasts
    contrasts(df$congruency) <- contrasts_to_run

    # Model
    model_poly_test <- glmer(
      afc_resp_acc ~ congruency * group +
        (congruency | participant) +
        (congruency | comic_name),
      data = df, family = binomial,
      control = glmerControl(optimizer = "bobyqa", optCtrl = list(maxfun = 100000))
    )

    # We can explore this model with "Anova" (capital A)
    print(summary(model_poly_test))
    return(model_poly_test)
  }

  # Use function
  red_model_2_ch <- group_poly_test(ret_data, "children", cbind(linear_comp, quadratic_comp))
  red_model_2_YA <- group_poly_test(ret_data, "YA", cbind(linear_comp, quadratic_comp))
  red_model_2_OA <- group_poly_test(ret_data, "OA", cbind(linear_comp, quadratic_comp))
}
