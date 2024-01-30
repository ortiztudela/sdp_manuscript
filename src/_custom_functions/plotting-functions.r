# Analysis of the memory tasks in SDP
# Author: Javier Ortiz-Tudela (Goethe Universitaet)
# October 2021
# Description:

## ----------------------  Set up  ----------------------------
# Load libraries
library(ggplot2)
library(lme4)
library(dplyr)

## ---------- Home-brewed function for plotting ---------------
spag_plot <- function(agg_data, y_var, chance_level, y_lab, title, y_lim=c(0,1), coeffs = NULL) {
  custom_plot <- ggplot(
    data = agg_data,
    aes(
      x = congruency, y = y_var, group = factor(participant),
      color = factor(participant)
    )
  ) +
    geom_line(alpha = 0.5) +
    facet_grid(cols = vars(factor(group, levels = c("children", "YA", "OA")))) +
    stat_summary(aes(x = congruency, y = y_var, group = group),
      fun = mean, geom = "point",
      shape = 20, size = 7, color = "red", fill = "red"
    ) +
    ylab(y_lab) +
    xlab("Ending type") +
    geom_hline(aes(yintercept = chance_level, colour = "red"),
      linetype = "dashed"
    ) +
    ylim(y_lim) +
    #labs(title = title) +
    theme(
      panel.grid.major = element_blank(),
      panel.grid.minor = element_blank()
    ) +
    theme_bw() +
    theme(
      legend.position = "none",
      text = element_text(size = 30)
    ) +
    theme(text = element_text(family = "Helvetica")) +
    scale_x_discrete(labels = c("Expected", "Neutral", "Unexpected")) +
    theme(axis.text.x = element_text(angle = 45, hjust = 1))


  # Add polynomial curves if coefficients are provided
  if (!is.null(coeffs)) {
    # Get the levels of the group variable from the data
    group_levels <- levels(agg_data$group)

    # Overlay the polynomial curves onto the base plot
    custom_plot <- add_poly_curves(custom_plot, coeffs, group_levels)
  }
  return(custom_plot)
}

# Function to add polynomial curves to the existing plot
add_poly_curves <- function(plot, coeffs, group_levels) {
  # Add polynomial curves based on coefficients for each group
  for (group in group_levels) {
    # Coefficients for the current group
    intercept <- coeffs[[group]]$intercept
    linear_coeff <- coeffs[[group]]$linear
    quadratic_coeff <- coeffs[[group]]$quadratic

    # Function for the polynomial curve
    poly_curve <- function(x) {
      intercept + linear_coeff * x + quadratic_coeff * x^2
    }

    # Creating a sequence of x-values for plotting
    x_range <- seq(from = -1, to = 1, length.out = 100)

    # Calculating y-values based on the polynomial curve
    y_values <- sapply(x_range, poly_curve)

    # Adjusting the x-values for plotting
    x_range <- x_range + 2

    # Creating a data frame for plotting
    curve_data <- data.frame(x = x_range, y = y_values, group = group)

    # Adding the curve to the plot
    plot <- plot +
      # geom_text(
      #   data = curve_data,
      #   aes(x = x, y = y, group = group, label = "*"),
      #   colour = "blue",
      #   size = 6 # Adjust the size as needed
      # )
      geom_line(
        data = curve_data,
        aes(x = x, y = y, group = group),
        colour = "blue", linetype = "twodash",
        linewidth = 2
      )
  }
  return(plot)
}

# Function to calculate adjusted intercepts for each group
calculate_intercepts <- function(model, fa_group_data = NULL) {
  # Initialize a list to store the intercepts
  intercepts <- list()

  # Get the levels of the group variable
  groups <- c("children", "YA", "OA")

  # Calculate the intercept for each group
  for (group in groups) {
    # Calculate the intercept for the current group from the model
    if (group == "children") {
      group_intercept <- plogis(fixef(model)["(Intercept)"])
    } else {
      group_intercept <- plogis(fixef(model)["(Intercept)"] +
        fixef(model)[paste0("group", group)])
    }
    # Adjust the intercept based on the FAs for the group if requested
    if (!is.null(fa_group_data)) {
      group_intercept <- group_intercept -
        fa_group_data$ov_fas[fa_group_data$group == group]
    }
    # Store the intercept in the list
    intercepts[[group]] <- group_intercept
  }
  return(intercepts)
}
