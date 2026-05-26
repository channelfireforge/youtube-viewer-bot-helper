package config

import (
	"os"
	"strconv"
)

type Config struct {
	MaxViews    int
	MinDelayMs  int
	MaxDelayMs  int
	FailureRate float64
}

func Load() *Config {
	cfg := &Config{
		MaxViews:    100,
		MinDelayMs:  100,
		MaxDelayMs:  500,
		FailureRate: 0.05,
	}

	if v := os.Getenv("BOT_MAX_VIEWS"); v != "" {
		if i, err := strconv.Atoi(v); err == nil {
			cfg.MaxViews = i
		}
	}
	if v := os.Getenv("BOT_MIN_DELAY_MS"); v != "" {
		if i, err := strconv.Atoi(v); err == nil {
			cfg.MinDelayMs = i
		}
	}
	if v := os.Getenv("BOT_MAX_DELAY_MS"); v != "" {
		if i, err := strconv.Atoi(v); err == nil {
			cfg.MaxDelayMs = i
		}
	}
	if v := os.Getenv("BOT_FAILURE_RATE"); v != "" {
		if f, err := strconv.ParseFloat(v, 64); err == nil {
			cfg.FailureRate = f
		}
	}

	return cfg
}