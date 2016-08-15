import sublime, sublime_plugin, os
import subprocess

class ArtisanHelp(sublime_plugin.TextCommand):
	def run(self, edit):

		folder = self.view.window().folders()[0]
		os.chdir(folder)

		self.view.window().run_command("exec", {
			"cmd" : ["php artisan help"],
			"shell" : True,
			"working_dir" : folder})

class ArtisanList(sublime_plugin.TextCommand):
	def run(self, edit):

		folder = self.view.window().folders()[0]
		os.chdir(folder)

		self.view.window().run_command("exec", {
			"cmd" : ["php artisan list"],
			"shell" : True,
			"working_dir" : folder})

class ArtisanUp(sublime_plugin.TextCommand):
	def run(self, edit):

		folder = self.view.window().folders()[0]
		os.chdir(folder)

		self.view.window().run_command("exec", {
			"cmd" : ["php artisan up"],
			"shell" : True,
			"working_dir" : folder})

class ArtisanDown(sublime_plugin.TextCommand):
	def run(self, edit):

		folder = self.view.window().folders()[0]
		os.chdir(folder)

		self.view.window().run_command("exec", {
			"cmd" : ["php artisan down"],
			"shell" : True,
			"working_dir" : folder})

class ArtisanTinker(sublime_plugin.TextCommand):
	def run(self, edit):

		folder = self.view.window().folders()[0]
		os.chdir(folder)

		self.view.window().run_command("exec", {
			"cmd" : ["osascript -e 'tell application \"Terminal\" to do script \"php "+folder+"/artisan tinker\"'"],
			"shell" : True,
			"working_dir" : folder})

class ArtisanOptimize(sublime_plugin.TextCommand):
	def run(self, edit):

		folder = self.view.window().folders()[0]
		os.chdir(folder)

		self.view.window().run_command("exec", {
			"cmd" : ["php artisan optimize"],
			"shell" : True,
			"working_dir" : folder})

class ArtisanEnv(sublime_plugin.TextCommand):
	def run(self, edit):

		folder = self.view.window().folders()[0]
		os.chdir(folder)

		self.view.window().run_command("exec", {
			"cmd" : ["php artisan env"],
			"shell" : True,
			"working_dir" : folder})

class Artisan(sublime_plugin.TextCommand):
	def run(self, edit):

		folder = self.view.window().folders()[0]
		os.chdir(folder)

		self.view.window().run_command("exec", {
			"cmd" : ["php artisan"],
			"shell" : True,
			"working_dir" : folder})

class ArtisanCreateProject(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("[Insert your Project name]", "", self.on_done, None, None)

	def on_done(self, generate_command):
		try:
			folder = self.window.folders()[0]
			os.chdir(folder)
			args = generate_command.split(" ")
			cmd = args[0]
			print ([cmd, args[0:]])		
			self.window.run_command("exec", {
				"cmd" : ["php /usr/local/bin/composer create-project --prefer-dist laravel/laravel " + cmd],
				"shell" : True,
				"working_dir" : folder})
		except ValueError:
			pass

class ArtisanApp(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("[name] [args]", "", self.on_done, None, None)

	def on_done(self, generate_command):
		try:
			folder = self.window.folders()[0]
			os.chdir(folder)
			args = generate_command.split(" ")
			cmd = args[0]
			print (["php", "artisan", cmd, args[0:]])
			self.window.run_command("exec", {
				"cmd" : ["php artisan app:name " + cmd],
				"shell" : True,
				"working_dir" : folder})
		except ValueError:
			pass

class ArtisanAuth(sublime_plugin.TextCommand):
	def run(self, edit):
		folder = self.view.window().folders()[0]
		os.chdir(folder)
		self.view.window().run_command("exec", {
			"cmd" : ["php artisan auth:clear-reset"],
			"shell" : True,
			"working_dir" : folder})

class ArtisanCache(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("[clear|table] [args]", "", self.on_done, None, None)
	def on_done(self, generate_command):
		try:
			folder = self.window.folders()[0]
			os.chdir(folder)
			args = generate_command.split(" ")
			cmd = 'cache:' + args[0]
			print (["php", "artisan", cmd, args[1:]])		
			self.window.run_command("exec", {
				"cmd" : ["php", "artisan", cmd] + args[1:],
				"shell" : False,
				"working_dir" : folder})
		except ValueError:
			pass

class ArtisanConfig(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("[cache|clear] [args]", "", self.on_done, None, None)
	def on_done(self, generate_command):
		try:
			folder = self.window.folders()[0]
			os.chdir(folder)
			args = generate_command.split(" ")
			cmd = 'config:' + args[0]
			print (["php", "artisan", cmd, args[1:]])		
			self.window.run_command("exec", {
				"cmd" : ["php", "artisan", cmd] + args[1:],
				"shell" : False,
				"working_dir" : folder})
		except ValueError:
			pass

class ArtisanDb(sublime_plugin.TextCommand):
	def run(self, edit):
		folder = self.view.window().folders()[0]
		os.chdir(folder)
		self.view.window().run_command("exec", {
			"cmd" : ["php artisan db:seed"],
			"shell" : True,
			"working_dir" : folder})

class ArtisanEvent(sublime_plugin.TextCommand):
	def run(self, edit):
		folder = self.view.window().folders()[0]
		os.chdir(folder)
		self.view.window().run_command("exec", {
			"cmd" : ["php artisan event:generate"],
			"shell" : True,
			"working_dir" : folder})

class ArtisanKey(sublime_plugin.TextCommand):
	def run(self, edit):
		folder = self.view.window().folders()[0]
		os.chdir(folder)
		self.view.window().run_command("exec", {
			"cmd" : ["php artisan key:generate"],
			"shell" : True,
			"working_dir" : folder})

class ArtisanMigrateCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		folder = self.view.window().folders()[0]
		os.chdir(folder)	
		self.view.window().run_command("exec", {
			"cmd" : ["php artisan migrate"],
			"shell" : True,
			"working_dir" : folder})

class ArtisanServeCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		folder = self.view.window().folders()[0]
		os.chdir(folder)
		self.view.window().run_command("exec", {
			"cmd" : ["pkill -9 php && php artisan serve"],
			"shell" : True,
			"working_dir" : folder})

class ArtisanServestopCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		folder = self.view.window().folders()[0]
		os.chdir(folder)
		self.view.window().run_command("exec", {
			"cmd" : ["pkill -9 php"],
			"shell" : True,
			"working_dir" : folder})

class ArtisanKey(sublime_plugin.TextCommand):
	def run(self, edit):
		folder = self.view.window().folders()[0]
		os.chdir(folder)
		self.view.window().run_command("exec", {
			"cmd" : ["php artisan key:generate"],
			"shell" : True,
			"working_dir" : folder})

class ArtisanMakeCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("[auth|console|controller|event|job|listener|middleware|migration|model|policy|provider|request|seeder|test] [args] [Es. controller name --resource]", "", self.on_done, None, None)
	def on_done(self, generate_command):
		try:
			folder = self.window.folders()[0]
			os.chdir(folder)
			args = generate_command.split(" ")
			cmd = 'make:' + args[0]
			print (["php", "artisan", cmd, args[1:]])
			self.window.run_command("exec", {
				"cmd" : ["php", "artisan", cmd] + args[1:],
				"shell" : False,
				"working_dir" : folder})
		except ValueError:
			pass

class ArtisanMigrateCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("[install|refresh|reset|rollback|status] [args]", "", self.on_done, None, None)
	def on_done(self, generate_command):
		try:
			folder = self.window.folders()[0]
			os.chdir(folder)
			args = generate_command.split(" ")
			cmd = 'migrate:' + args[0]
			print (["php", "artisan", cmd, args[1:]])	
			self.window.run_command("exec", {
				"cmd" : ["php", "artisan", cmd] + args[1:],
				"shell" : False,
				"working_dir" : folder})
		except ValueError:
			pass

class ArtisanQueueCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("[failed|failed-table|flush|forget|listen|restart|retry|table|work] [args]", "", self.on_done, None, None)
	def on_done(self, generate_command):
		try:
			folder = self.window.folders()[0]
			os.chdir(folder)
			args = generate_command.split(" ")
			cmd = 'queue:' + args[0]
			print (["php", "artisan", cmd, args[1:]])
			self.window.run_command("exec", {
				"cmd" : ["php", "artisan", cmd] + args[1:],
				"shell" : False,
				"working_dir" : folder})
		except ValueError:
			pass

class ArtisanRouteCommand(sublime_plugin.WindowCommand):
	def run(self):
		self.window.show_input_panel("[cache|registration|clear|list] [args]", "", self.on_done, None, None)
	def on_done(self, generate_command):
		try:
			folder = self.window.folders()[0]
			os.chdir(folder)
			args = generate_command.split(" ")
			cmd = 'route:' + args[0]
			print (["php", "artisan", cmd, args[1:]])
			self.window.run_command("exec", {
				"cmd" : ["php", "artisan", cmd] + args[1:],
				"shell" : False,
				"working_dir" : folder})
		except ValueError:
			pass

class ArtisanSchedule(sublime_plugin.TextCommand):
	def run(self, edit):
		try:
			folder = self.view.window().folders()[0]
			os.chdir(folder)
			self.view.window().run_command("exec", {
				"cmd" : ["php", "artisan", "schedule:run"],
				"shell" : False,
				"working_dir" : folder})
		except ValueError:
			pass

class ArtisanSession(sublime_plugin.TextCommand):
	def run(self, edit):
		try:
			folder = self.view.window().folders()[0]
			os.chdir(folder)
			self.view.window().run_command("exec", {
				"cmd" : ["php", "artisan", "session:table"],
				"shell" : False,
				"working_dir" : folder})
		except ValueError:
			pass

class ArtisanVendor(sublime_plugin.TextCommand):
	def run(self, edit):
		try:
			folder = self.view.window().folders()[0]
			os.chdir(folder)
			self.view.window().run_command("exec", {
				"cmd" : ["php", "artisan", "vendor:publish"],
				"shell" : False,
				"working_dir" : folder})
		except ValueError:
			pass

class ArtisanView(sublime_plugin.TextCommand):
	def run(self, edit):
		try:
			folder = self.view.window().folders()[0]
			os.chdir(folder)
			self.view.window().run_command("exec", {
				"cmd" : ["php", "artisan", "view:clear"],
				"shell" : False,
				"working_dir" : folder})
		except ValueError:
			pass
