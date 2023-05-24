# yesc_bulk


Bulk packager for operating yesc to package items from `sqlite` database with parameters set via `config.ini`

#### Example usage
`$ python3 yesc_bulk.py`




### sqlite database

```sql
CREATE TABLE "entities" (
	"input"	TEXT,
	"aspace_title"	TEXT,
	"ao_ref"	TEXT,
	"security_tag"	TEXT,
	"protocol_ref"	TEXT,
	"packaged_date"	TEXT,
	"size_bytes"	TEXT,
	"filecount"	TEXT
)
```

### config.ini

```yaml
[example default]
db_name = dbname.db

input =   
output =   
securitytag = 
parent = 
aspace = 
prefix = 
sotitle = 
iotitle = 
sodescription = 
iodescription = 
sometadata = 
iometadata = 
ioidtype = 
ioidvalue = 
soidtype = 
soidvalue = 
sipconfig = 
excludedFileNames = 
storage =  
storageconfig = 

# leave empty for False, True to pass option
assetonly = 
singleasset = 
export = 
representations = 
md5 = 
sha1 = 
sha256 = 
sha512 = 

```


#### Contact:
David Cirella  
[github.com/decirella](https://github.com/decirella)
