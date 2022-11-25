package $$MOD_AUTHOR.$$MOD_ID.forge;

import org.slf4j.Logger;

import com.mojang.logging.LogUtils;

import net.minecraftforge.common.MinecraftForge;

import net.minecraftforge.fml.common.Mod;

@Mod("$$MOD_ID")
public class $$MOD_NAME {
    private static final Logger LOGGER = LogUtils.getLogger();

    public $$MOD_NAME() {
        MinecraftForge.EVENT_BUS.register(this);

        LOGGER.info("$$MOD_NAME initialized");
    }
}
