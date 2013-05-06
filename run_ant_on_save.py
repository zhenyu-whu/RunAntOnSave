import sublime, sublime_plugin, os

class BuildonSave(sublime_plugin.EventListener):
	def on_post_save(self, view):
		folder = os.path.dirname(view.file_name())
		
		#let's see if project wants to be autobuild 
		os.chdir(folder);

		if(os.path.exists('build.xml')):
			view.window().run_command('exec', {'cmd':['ant.bat'], 'working_dir': folder})			
			view.window().run_command("hide_panel", {"panel": "output.exec"})
			print 'Build Successfully!'
		


