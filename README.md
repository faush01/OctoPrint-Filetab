# OctoPrint-Filetab

Moves the files list from the side bar to a main tab.

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)

## Configuration

No config.

Works best with the Octoprint Custom CSS plugin with the following CSS overrides:

```
.octoprint-container.container {
  width: 90%;
}

.octoprint-container .row {
  display: flex;
  flex-direction: row;
}

.octoprint-container .row .span8 {
  flex-grow: 2;
}

#files > div.gcode_files > div.scroll-wrapper {
  height: 600px;
}
```


