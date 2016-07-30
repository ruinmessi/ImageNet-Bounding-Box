user=''
akey=''
syn=''
url="www.image-net.org/download/synset?wnid=$syn&username=$user&accesskey=$akey&release=latest&src=stanford"

#wget -O $syn.tar $url

while read line; do
    ((co++))
done < list.txt #MODIFIED FILE.TXT TO LIST.TXT
echo $co

while read line; do
    syn=$line
    if ((var >= co)); then
    	url="www.image-net.org/download/synset?wnid=$syn&username=$user&accesskey=$akey&release=latest&src=stanford"
    	wget -O $syn.tar $url
    	printf "$syn\n" >> list.txt #MODIFIED FILE.TXT TO LIST.TXT
    fi
    ((var++))
done < synset_id_list
