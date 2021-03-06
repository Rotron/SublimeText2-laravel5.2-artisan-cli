# SublimeText2-laravel5.2-artisan-cli

Sublime Text plugin to replace Laravel 5.2 Artisan CLI

This plugin allows you the run the normal Artisan CLI using the Sublime Text interface,
without having to open and use the command line.
------------------------------------------------------------------------------------------------------------------
Options Available:

NEW! - Implementation for Stop and Serve Php development server.
NEW! - Composer Laravel Install
NEW! - Tinker with interactive Shell

Available commands:

       Tinker              Open a Terminal window Psy Shell                                      NEW!
       Composer            Install a new Laravel Project                                         NEW!
       Serve               Serve the application on the PHP development server -                 NEW!
       STOP Serve          Stop the application on the PHP development server -                  NEW!
       clear-compiled      Remove the compiled class file                                  
       down                Put the application into maintenance mode
       env                 Display the current framework environment
       help                Displays help for a command
       list                Lists commands
       migrate             Run the database migrations
       optimize            Optimize the framework for better performance                   
       tinker              Interact with your application                                  
       up                  Bring the application out of maintenance mode
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

<img src ="https://camo.githubusercontent.com/11f388b66e7aa33b8b81ec410b60054aeaecbc6c/687474703a2f2f672e7265636f726469742e636f2f31345845424356764c4e2e676966">

1). Copy sublime-artisa inside the Packages Folder.

    Follow this for get the Package Folder

    MacOsx
    Sublime Text2 -> Preferences -> Browse Packages..

2) For create a new Laravel Project

<img src ="https://camo.githubusercontent.com/eb7422d18e4085a982b150fbb1991d674fed9518/687474703a2f2f672e7265636f726469742e636f2f54396d51643067514b362e676966">

Just press Cmd + Shift + P for the dropdown command list, and search for composer.

Or

NOTE: 
At the current moment,
for the plugin to run correctly the artisan file
needs to been in the root folder of your structure in the Side bar.

------------------------------------------------------------------------------------------------------------------

Give some feedback.

Thanks.

Federico Saccà
