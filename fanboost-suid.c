#include <stdio.h>
#include <sys/types.h>
#include <sys/stat.h>
#include <unistd.h>
#include <stdlib.h>
#include <string.h>

// help information
void help() {
	puts("Usage: fanboost [option]\n");
	puts("Available Options:");
	puts("  help\t\tshow this help information");
	puts("  status\tshow whether fanboost mode is on or off");
	puts("  on\t\tenable fanboost mode");
	puts("  off\t\tdisable fanboost mode");
	return;
}

int main(int argc, char** argv) {
	// parse option
	char* fbm_config = "/sys/devices/platform/asus-nb-wmi/fan_boost_mode";
	int mode;
	if(argc == 2) {
		if(strcmp(argv[1], "help") == 0) {
			help();
			return 0;
		} else if(strcmp(argv[1], "status") == 0) {
			mode = 0;
		} else if(strcmp(argv[1], "on") == 0) {
			mode = 1;
		} else if(strcmp(argv[1], "off") == 0) {
			mode = 2;
		} else {
			puts("Invalid option.");
			help();
			return 1;
		}
	} else {
		help();
		return 1;
	}
	
	// set uid to 0 (root) (in order to utilize suid bit)
	uid_t uid_orig = getuid();
	setuid(0);
	if(getuid()) {
		puts("error: needs root permission.");
		return 1;
	}
	
	// open file
	FILE* fp = fopen(fbm_config, "r+");
	if(fp == NULL) {
		printf("error: cannot open file \"%s\".\n", fbm_config);
		return 1;
	};
	
	// file operation
	switch(mode) {
		case 0:
			char c = fgetc(fp);
			if(c=='0') {
				puts("OFF");
			} else if (c=='1') {
				puts("ON");
			} else {
				puts("UNKNOWN");
			}
			break;
		case 1:
			fputc('1', fp);
			break;
		case 2:
			fputc('0', fp);
			break;
	}
	
	// finalizing
	fclose(fp);
	setuid(uid_orig);
	return 0;
}
