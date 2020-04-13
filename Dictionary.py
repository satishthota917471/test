envDictioanry  = repository.read('Environments/Dev/Testing’)
dictEntries = envDictioanry.entries
manifestfile = open("/tmp/manifest.txt", "r")
for entry in manifestfile:
    filepathentry = entry.split("=")
    if len(filepathentry) == 2:
        dictEntries.update({filepathentry[0] : filepathentry[1]})
repository.update(envDictioanry)
print "Done"