# Mod
name = "$$MOD_NAME";
version = "$$MOD_VERSION";
author = "$$MOD_AUTHOR";
description = "$$MOD_DESCRIPTION";
url = "$$MOD_URL";
src = "$$MOD_SOURCES";
License = "$$MOD_LICENSE";

# Workspace
class group:
    fabric = author+"."+name+"-"+"fabric";
    forge = author+"."+name+"-"+"forge";