
# Makefile to work phd repository
#
# @author Medvedev Ilya
# @email imedvedev@elvees.com


# TARGETS

clean:
	# clean temporal files
	@find . -name "*~" -exec rm -rf {} \;
	@find . -name "*.swp" -exec rm -rf {} \;

