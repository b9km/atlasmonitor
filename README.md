# atlasmonitor
What is atlasmonitor ?

a simple tool that can be used to track live system information like cpu ram and disk , inside the terminal .

why atlasmonitor?

it was designed mainly for my homelab , where there was no real way to track resources in real time . atlasmonitor solved that problem since it runs on the terminal , displays useful information and could be used by ubuntu-server users and any computer user in general .


## Features

- Live CPU usage
- Live RAM usage
- Live Disk usage
- Battery percentage
- Hostname detection
- Operating system detection
- Cross-platform (Windows & Linux)

## Installation

Clone the repository:

```bash
git clone https://github.com/b9km/atlasmonitor.git
```

Install the dependencies:

```bash
pip install -r requirements.txt
```

Install Atlas Monitor:

```bash
pip install .
```

## Usage

Run:

```bash
atlasmonitor
```

Press `Ctrl+C` to exit.

## Project Status

Current version:

**v0.2 Beta**

## Roadmap

- Better terminal interface
- Battery health information
- Network statistics
- CPU temperature
- Multiple machine monitoring

