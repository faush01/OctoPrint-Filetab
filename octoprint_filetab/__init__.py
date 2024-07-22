import octoprint.plugin

class FiletabPlugin(octoprint.plugin.TemplatePlugin, octoprint.plugin.AssetPlugin):
    def get_template_configs(self):
        return [
            dict(type="tab", name="Files")
        ]

    def get_assets(self):
        return dict(css=["css/filetab.css"])

__plugin_name__ = "FileTab"
__plugin_version__ = "0.0.1"
__plugin_pythoncompat__ = ">=2.7,<4"

__plugin_implementation__ = FiletabPlugin()
__plugin_settings_overlay__ = dict(appearance=dict(components=dict(disabled=dict(sidebar=["files"]))))
