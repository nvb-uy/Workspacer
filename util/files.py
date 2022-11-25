# Common files that both loaders use.
common = [
    "gradlew",
    "gradlew.bat",
    "gradle/wrapper/gradle-wrapper.properties",
    "gradle/wrapper/gradle-wrapper.jar",
    ".github/workflows/build.yml"
]

# List of files that need placeholder replacement.
class placeholder:
    fabric = [
        "fabric.mod.json",
        "$$MOD_ID.mixins.json"
        "$$MOD_ID.java",
        "MyMixin.java",
        "build.gradle",
        "gradle.properties"
    ];
    forge = [
        "mods.toml",
        "$$MOD_ID.mixins.json"
        "$$MOD_ID.java",
        "MyMixin.java",
        "build.gradle",
        "gradle.properties",
        "pack.mcmeta"
    ];