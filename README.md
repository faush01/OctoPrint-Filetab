# OctoPrint-Filetab

Moves the files list from the side bar to a main tab.

This plugin is based on the files avialable from: 
https://gist.github.com/foosel/86157172899666cc0658

## Setup

Install via the bundled [Plugin Manager](https://docs.octoprint.org/en/master/bundledplugins/pluginmanager.html)

## Configuration

No config.

Works best with the Octoprint Custom CSS plugin with the following CSS overrides: 
https://plugins.octoprint.org/plugins/customcss/

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


