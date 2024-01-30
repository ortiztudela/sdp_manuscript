# Figures of the polynomial components of the memory tasks in SDP
# Author: Javier Ortiz-Tudela (Goethe Universitaet / University of Granada)
# October 2021
# Description:

## ----------------------  Set up  ----------------------------
# Load libraries
library(ggplot2)
library(ggpattern)

# Set working directory
main_dir <- paste(getwd(), "../", sep = "/")

# Where do you want the plots?
fig_dir <- paste(main_dir, "results/figures/retrieval/", sep = "/")

## ----------------------  Get data ----------------------------
# Create a data frame with the coefficients and their respective confidence intervals
# Here I'm taking the info from the winning model in ending_recog.R
ending_recog_coefficients <- data.frame(
  AgeGroup = rep(c("Children", "Young Adults", "Older Adults"), each = 2),
  Component = rep(c("Linear", "Quadratic"), times = 3),
  Estimate = c(.673, .369, .618, .192, -0.285, .117),
  StdError = c(.11317, .06159, .11144, .06133, .10826, .06099)
)

# Data for cue recognition
cue_recog_coefficients <- data.frame(
  AgeGroup = rep(c("Children", "Young Adults", "Older Adults"), each = 2),
  Component = rep(c("Linear", "Quadratic"), times = 3),
  Estimate = c(.143, .085, .180, .088, .046, .032),
  StdError = c(.059, .034, .061, .034, .062, .036)
)

# Data for outcome memory
outcome_memory_coefficients <- data.frame(
  AgeGroup = rep(c("Children", "Young Adults", "Older Adults"), each = 2),
  Component = rep(c("Linear", "Quadratic"), times = 3),
  Estimate = c(.0, .0, .469, .020, .0, .0),
  StdError = c(.0, .0, .141, .063, .0, .0)
)

compute_ci <- function(coefficients, alpha = 0.05) {
  # Compute the critical value for the confidence interval
  cv <- qnorm(1 - alpha / 2)

  # Calculate confidence intervals manually
  coefficients$LowerCI <- coefficients$Estimate - cv * coefficients$StdError
  coefficients$UpperCI <- coefficients$Estimate + cv * coefficients$StdError

  # Return the coefficients with the confidence intervals
  return(coefficients)
}

# Compute confidence intervals for the ending recognition coefficients
ending_recog_coefficients <- compute_ci(ending_recog_coefficients)

# Compute confidence intervals for the cue recognition coefficients
cue_recog_coefficients <- compute_ci(cue_recog_coefficients)

# Compute confidence intervals for the outcome memory coefficients
outcome_memory_coefficients <- compute_ci(outcome_memory_coefficients)

# Make sure the AgeGroup is a factor with levels in the correct order for plotting for both data frames
cue_recog_coefficients$AgeGroup <- factor(cue_recog_coefficients$AgeGroup,
  levels = c("Children", "Young Adults", "Older Adults")
)
ending_recog_coefficients$AgeGroup <- factor(ending_recog_coefficients$AgeGroup,
  levels = c("Children", "Young Adults", "Older Adults")
)
outcome_memory_coefficients$AgeGroup <- factor(outcome_memory_coefficients$AgeGroup,
  levels = c("Children", "Young Adults", "Older Adults")
)

## ----------------------  Plot data ----------------------------
# Function to plot the coefficients
barplot_coefficients <- function(coefficients, title, is_legend) {
  ggplot(coefficients, aes(x = AgeGroup, y = Estimate, fill = Component)) +
    geom_bar_pattern(
      aes(pattern = Component), # Move pattern aes here
      stat = "identity",
      position = position_dodge(width = 0.8),
      width = 0.7,
      pattern_density = 0.1, # Control the density of the pattern
      pattern_spacing = 0.09, # Control the spacing between pattern elements
      pattern_key_scale_factor = 0.9, # Control the size of pattern in the legend key
      color = "black" # Outline color for bars
    ) +
    scale_fill_manual(
      values = c("Linear" = "#E1BE6A", "Quadratic" = "#40B0A6") # Set the colors here
    ) +
    scale_pattern_manual(
      values = c(
        "Linear" = "stripe",
        "Quadratic" = "wave"
      ),
    ) +
    geom_errorbar(
      aes(ymin = LowerCI, ymax = UpperCI, group = Component),
      position = position_dodge(width = 0.8),
      width = 0.25
    ) +
    labs(y = "Coefficient Estimate", x = "Age Group", fill = "Component", pattern = "Component") +
    theme_minimal() +
    geom_hline(yintercept = 0, linetype = "dashed") +
    theme(text = element_text(size = 15)) +
    ggtitle(title) +
    theme(legend.position = is_legend) +
    ylim(-0.6, 1) +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))
}

## ------------------------------------------------------------------
## -----------  Creat plots for each memory task --------------------
## ------------------------------------------------------------------

# Plotting the cue recognition coefficients
cue_recog_plot <- barplot_coefficients(
  coefficients = cue_recog_coefficients,
  title = "A. Cue Recognition",
  is_legend = "right"
)

# Plotting the ending recognition coefficients
ending_recog_plot <- barplot_coefficients(
  coefficients = ending_recog_coefficients,
  title = "B. Ending Recognition",
  is_legend = "right"
)

# Plotting the outcome memory coefficients
outcome_memory_plot <- barplot_coefficients(
  coefficients = outcome_memory_coefficients,
  title = "C. Outcome Memory",
  is_legend = "right"
)
# Arrange both plots into a single figure
library(gridExtra)
final_plot <- grid.arrange(cue_recog_plot, ending_recog_plot, nrow = 1, ncol = 2)

# Saving the final plot
plot_filename <- paste(fig_dir, "polynomials-lmm.pdf", sep = "/")
ggsave(plot_filename, final_plot)
