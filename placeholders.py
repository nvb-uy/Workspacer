# Placeholders are strings that start with $$ and are replaced later on
# after setting up the workspace. They are vital for the mod's development.

# Mod Placeholders
name = "$$MOD_NAME"; # The name of the mod (Ex. "My Mod")
version = "$$MOD_VERSION"; # Starting version of the mod (Ex. "1.0.0")
author = "$$MOD_AUTHOR"; # The author of the mod (Ex. "ElocinDev")
description = "$$MOD_DESCRIPTION"; # A description of the mod (Ex. "A mod that adds a new block")
url = "$$MOD_URL"; # Main URL of the mod (ex. CurseForge page)
src = "$$MOD_SOURCES"; # The source code of the mod (ex. GitHub repo)
License = "$$MOD_LICENSE"; # The license of the mod (ex. MIT)

# Workspace Placeholders
class group: # The group is the folder structure of the mod (Ex. "ElocinDev/mymod/fabric")
    fabric = author+"."+name+"."+"fabric";
    forge = author+"."+name+"."+"forge";