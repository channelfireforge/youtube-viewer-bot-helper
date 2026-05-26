package main

import (
	"fmt"
	"log"
	"os"

	"github.com/user/youtube-viewer-bot-helper/bot"
)

func main() {
	videoURL := os.Getenv("YOUTUBE_VIDEO_URL")
	if videoURL == "" {
		log.Fatal("YOUTUBE_VIDEO_URL environment variable is required")
	}

	viewer := bot.NewViewer(videoURL)
	count, err := viewer.Run()
	if err != nil {
		log.Fatalf("Bot failed: %v", err)
	}

	fmt.Printf("Successfully generated %d views for %s\n", count, videoURL)
}