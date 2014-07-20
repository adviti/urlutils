fuction isValidUrl(url)
{
    var isvalid = 0;
    starting_with = url.substr(0,9);
    substr1 = starting_with;
    substr2 = starting_with(0, 8);
    if(substr1 == "https://" or substr2 == "http://")
        isvalid = 1
    if isvalid==0
        document.write("invalid url");
        return false;
    else
        return true;

}