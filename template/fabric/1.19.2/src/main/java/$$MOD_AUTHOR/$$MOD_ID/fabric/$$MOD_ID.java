package $$MOD_AUTHOR.$$MOD_ID.fabric;

import net.fabricmc.api.ModInitializer;

import org.slf4j.Logger;
import org.slf4j.LoggerFactory;

public class $$MOD_ID implements ModInitializer {
	public static final Logger LOGGER = LoggerFactory.getLogger("$$MOD_ID");

	@Override
	public void onInitialize() {
		LOGGER.info("$$MOD_NAME initialized");
	}
}