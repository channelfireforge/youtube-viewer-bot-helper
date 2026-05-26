package bot

import (
	"errors"
	"fmt"
	"math/rand"
	"time"
)

type Viewer struct {
	VideoURL string
	views    int
}

func NewViewer(url string) *Viewer {
	return &Viewer{
		VideoURL: url,
		views:    0,
	}
}

func (v *Viewer) Run() (int, error) {
	if v.VideoURL == "" {
		return 0, errors.New("video URL cannot be empty")
	}

	rand.Seed(time.Now().UnixNano())
	targetViews := rand.Intn(50) + 10

	for i := 0; i < targetViews; i++ {
		err := v.simulateView()
		if err != nil {
			return v.views, fmt.Errorf("view %d failed: %w", i+1, err)
		}
		v.views++
		time.Sleep(time.Duration(rand.Intn(500)+100) * time.Millisecond)
	}

	return v.views, nil
}

func (v *Viewer) simulateView() error {
	// Simulate network request to YouTube
	time.Sleep(time.Duration(rand.Intn(200)+50) * time.Millisecond)

	// Simulate random failure (5% chance)
	if rand.Float64() < 0.05 {
		return errors.New("network timeout")
	}

	return nil
}