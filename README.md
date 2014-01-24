This project is used to perform automatic builds on the Jenkins CI server.

Usage:
 1. Create a working directory (ex: /opt/working_dir)
 2. Run setup.eclipse.sh
 3. Run build.orcc.sh
 4. Run run.orcc.sh or run.simulator.sh

Example:
```sh
mkdir /opt/working_dir
./setup.eclipse.sh /opt/working_dir
./build.orcc.sh /opt/working_dir ~/gitprojects/orcc/eclipse/feature ~/gitprojects/orcc/eclipse/plugins ~/gitprojects/orcc/eclipse/bundles ~/gitprojects/xronos/eclipse/plugins
./run.orcc.sh /opt/working_dir ~/gitprojects/orc-apps c RVC org.sc29.wg11.mpeg4.part10.php.Top_mpeg4_part10_PHP_decoder ~/cal_outputs
```

Command line options are available for each script by running it without options
