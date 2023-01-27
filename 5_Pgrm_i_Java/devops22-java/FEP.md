# Frequently Encountered Problems

(in java)

## Folder Names

* When dealing with java projects, stick to using letters in your folder names.
* Underscores are okay if you need to separate words.
* DO NOT use dots or spaces.

### Visual Studio Code - Color Theme

* Do not use any of the default color themes for VSCode when working with java as they do not have enough colors to work properly with the highlighting provided by the java extensions.
* All other standard included themes work fine.
* Does not work:
  * Light
  * Light+
  * Dark
  * Dark+
* Works:
  * Monokai
  * Monokai Dimmed
  * Abyss
  * Kimbie Dark
  * Quiet Light
  * Solarized Light

### Apache Maven

If you install with `brew` on mac you may have issues with the java version used for maven.

```bash
# Test with maven --version which java it uses
mvn --version

# If your correct java is set for libexec
$(/usr/libexec/java_home)/bin/java --version

# You can modify 
vim /usr/local/Cellar/maven/3.6.3_1/bin/mvn
```

Set mvn to this, *NOTE* your version may differ

```text
JAVA_HOME="${JAVA_HOME:-$(/usr/libexec/java_home)}" exec "/usr/local/Cellar/maven/3.6.3_1/libexec/bin/mvn"  "$@"
```
