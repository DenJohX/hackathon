/**
 * Created by cheves05 on 7/12/14.
 */
var gdpData={};
var ParseJsonP =function(data)
{
    var scale=0;
    gdpData = {};
    for(pais in data[1]) {
        if(data[1][pais].value !== null)
            gdpData[data[1][pais].country.id] = data[1][pais].value;
    }
    ConfMap(scale);
}

function GetData(data_type) {
    var scale=0;
    var url="";
    //Number of neonatal deaths
    if(data_type=="Health")
        url ="http://api.worldbank.org/countries/indicators/SH.DTH.NMRT?per_page=3800&date=2012:2014&format=jsonP&prefix=getdata";
    //Lower secondary completion rate, total EDUCATION
    if(data_type=="Education")
        url ="http://api.worldbank.org/countries/indicators/SE.SEC.CMPT.LO.ZS?per_page=3000&date=2005:2014&format=jsonP&prefix=getdata";
    //pobreza per capita $1.25/dia poverty
    if(data_type=="Poverty")
        url = 'http://api.worldbank.org/countries/indicators/SI.POV.GAPS?per_page=10000&date=2000:2014&format=jsonP&prefix=getdata';
    $.ajax({
        url : url,
        dataType:"jsonp",
        jsonpCallback:"getdata",
        success: ParseJsonP
    });
    if(data_type="Health")
        scale=1;
    else
        scale=0;

}
function ConfMap(scale_type)
{
    var scale;
    if(scale_type==1)
        scale=['#B71C1C','#4CAF50']; //entre mayor el numero mas rojo
    if(scale_type==0)
        scale=['#4CAF50','#B71C1C']; //entre mayor el numero mas verde
    $('#world-map').vectorMap({
        map: 'world_mill_en',
        series: {
            regions: [{
                values: gdpData,
                scale: ['#B71C1C','#4CAF50'],
                normalizeFunction: 'logaritmic'
            }]
        },
        backgroundColor: '#80DEEA',
        onRegionTipShow: function(e, el, code){
            el.html(el.html()+' ('+gdpData[code]+')');
        }
    });
}
