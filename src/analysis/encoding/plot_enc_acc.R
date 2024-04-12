# Plots of the encoding task in SDP
# Author: Javier Ortiz-Tudela (Goethe Universitaet)
# October 2021

plot_enc_acc <- function(root_dir) {
  ## ----------------------  Set up  ----------------------------
  # Load libraries
  library(dplyr)
  library(ggplot2)

  ## ----------------------  Load data ----------------------------
  # Where is the data?
  bids_dir <- paste(root_dir, "../data/BIDS/full_sample/", sep = "/")

  # Where do you want the plots?
  fig_dir <- paste(root_dir, "../figures/encoding/", sep = "/")

  # Create folder if it doesn't exist
  if (!dir.exists(fig_dir)) {
    dir.create(fig_dir)
  }

  # List data files
  filename <- "full-sample_task-sdp_beh.csv"

  # Read data from file
  enc_data <- read.csv(paste(bids_dir, filename, sep = "/"))

  ## ------------------------------------------------------------------
  ## ------------------ Overall Encoding accuracy ---------------------
  ## ------------------------------------------------------------------
  agg_data_ov <- enc_data %>%
    filter(OvsN == "old") %>%
    group_by(group, participant) %>%
    summarise(av_acc = mean(enc_acc))

  # Reordering group factor levels
  agg_data_ov$group <- factor(agg_data_ov$group,
    levels = c("children", "YA", "OA")
  )

  # Plot
  ggplot(
    data = agg_data_ov,
    aes(x = group, y = av_acc)
  ) +
    geom_point(size = 1, alpha = 0.6) +
    ylab("Proportion correct") +
    ylim(c(0.5, 1)) +
    theme_bw() +
    theme(
      panel.grid.major = element_blank(),
      panel.grid.minor = element_blank()
    ) +
    theme(text = element_text(size = 20)) +
    ggtitle("Overall encoding acc") +
    xlab("Age group")
  ggsave(paste(fig_dir, "enc_acc_overall.pdf", sep = "/"))


  ## ------------------------------------------------------------------
  ## ------------------ Encoding accuracy by congruity ----------------
  ## ------------------------------------------------------------------
  agg_data <- enc_data %>%
    filter(OvsN == "old") %>%
    group_by(group, participant, congruency) %>%
    summarise(av_acc = mean(enc_acc))

  # Reordering group factor levels
  agg_data$group <- factor(agg_data$group,
    levels = c("children", "YA", "OA")
  )
  # Sort the levels
  agg_data$congruency <- factor(agg_data$congruency,
    levels = c("con", "neu", "inc")
  )

  # Plot
  ggplot(
    data = agg_data,
    aes(
      x = congruency, y = av_acc,
      group = factor(participant), color = factor(participant)
    )
  ) +
    geom_line(alpha = 0.5) +
    theme(legend.position = "none") +
    facet_grid(cols = vars(group)) +
    ylim(c(0, 1)) +
    ylab("Proportion correct") +
    theme_bw() +
    theme(
      legend.position = "none",
      text = element_text(size = 20)
    ) +
    theme(text = element_text(family = "Helvetica")) +
    xlab("Ending type") +
    scale_x_discrete(labels = c("Expected", "Neutral", "Unexpected")) +
    theme(axis.text.x = element_text(angle = 45, hjust = 1)) +
    labs(title = paste("Encoding acc"))
  ggsave(paste(fig_dir, "enc_acc_cong.pdf", sep = "/"))
}
