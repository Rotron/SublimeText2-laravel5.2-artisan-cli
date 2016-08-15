# SublimeText2-laravel5.2-artisan-cli

Sublime Text plugin to replace Laravel 5.2 Artisan CLI

This plugin allows you the run the normal Artisan CLI using the Sublime Text interface,
without having to open and use the command line.
------------------------------------------------------------------------------------------------------------------
Options Available:

NEW! - Implementation for Stop and Serve Php development server.
NEW! - Composer Laravel Install

Available commands:
       Composer            Install a new Laravel Project                                         NEW!
       Serve               Serve the application on the PHP development server -                 NEW!
       STOP Serve          Stop the application on the PHP development server -                  NEW!
       clear-compiled      Remove the compiled class file                                  (IN DEVELOPMENT)
       down                Put the application into maintenance mode                       (IN DEVELOPMENT)
       env                 Display the current framework environment                       (IN DEVELOPMENT)
       help                Displays help for a command                                     (IN DEVELOPMENT)
       list                Lists commands                                                  (IN DEVELOPMENT)
       migrate             Run the database migrations
       optimize            Optimize the framework for better performance                   (IN DEVELOPMENT)
       tinker              Interact with your application                                  (IN DEVELOPMENT)
       up                  Bring the application out of maintenance mode                   (IN DEVELOPMENT)
      app
       app:name            Set the application namespace
      auth
       auth:clear-resets   Flush expired password reset tokens
      cache
       cache:clear         Flush the application cache
       cache:table         Create a migration for the cache database table
      config
       config:cache        Create a cache file for faster configuration loading
       config:clear        Remove the configuration cache file
      db
       db:seed             Seed the database with records
      event
       event:generate      Generate the missing events and listeners based on registration
      key
       key:generate        Set the application key
      make
       make:auth           Scaffold basic login and registration views and routes
       make:console        Create a new Artisan command
       make:controller     Create a new controller class
       make:event          Create a new event class
       make:job            Create a new job class
       make:listener       Create a new event listener class
       make:middleware     Create a new middleware class
       make:migration      Create a new migration file
       make:model          Create a new Eloquent model class
       make:policy         Create a new policy class
       make:provider       Create a new service provider class
       make:request        Create a new form request class
       make:seeder         Create a new seeder class
       make:test           Create a new test class
      migrate
       migrate:install     Create the migration repository
       migrate:refresh     Reset and re-run all migrations
       migrate:reset       Rollback all database migrations
       migrate:rollback    Rollback the last database migration
       migrate:status      Show the status of each migration
      queue
       queue:failed        List all of the failed queue jobs
       queue:failed-table  Create a migration for the failed queue jobs database table
       queue:flush         Flush all of the failed queue jobs
       queue:forget        Delete a failed queue job
       queue:listen        Listen to a given queue
       queue:restart       Restart queue worker daemons after their current job
       queue:retry         Retry a failed queue job
       queue:table         Create a migration for the queue jobs database table
       queue:work          Process the next job on a queue
      route
       route:cache         Create a route cache file for faster route registration
       route:clear         Remove the route cache file
       route:list          List all registered routes
      schedule
       schedule:run        Run the scheduled commands
      session
       session:table       Create a migration for the session database table
      vendor
       vendor:publish      Publish any publishable assets from vendor packages
      view
       view:clear          Clear all compiled view files
  
INSTALLATION

1). Copy sublime-artisa inside the Packages Folder.

    Follow this for get the Package Folder

    MacOsx
    Sublime Text2 -> Preferences -> Browse Packages..

2) For create a new Laravel Project

Just press Cmd + Shift + P for the dropdown command list, and search for composer.

Or

NOTE: 
At the current moment,
for the plugin to run correctly the artisan file
needs to been in the root folder of your structure in the Side bar.

------------------------------------------------------------------------------------------------------------------

Give some feedback.
Thanks.
