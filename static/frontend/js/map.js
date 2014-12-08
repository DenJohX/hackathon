/**
 * Created by cheves05 on 7/12/14.
 */

function GetData(data_type) {
    var gdpData={};
    var scale_type = 0;
    var normalize_function = 'lineal';
    var ParseJsonP = function(data)
    {
        gdpData = {};
        for(pais in data[1]) {
            if(data[1][pais].value !== null)
                gdpData[data[1][pais].country.id] = data[1][pais].value;
        }
        ConfMap();
    }

    var ConfMap = function()
    {
        var scale;
        if(scale_type==1)
            scale=['#B71C1C','#4CAF50']; //entre mayor el numero mas rojo
        if(scale_type==0)
            scale=['#4CAF50','#B71C1C']; //entre mayor el numero mas verde
        $('#world-map').empty().vectorMap({
            map: 'world_mill_en',
            series: {
                regions: [{
                    values: gdpData,
                    scale: scale,
                    normalizeFunction: normalize_function
                }]
            },
            backgroundColor: 'transparent',
            onRegionTipShow: function(e, el, code){
                el.html(el.html()+' ('+gdpData[code]+')');
            }
        });
    }

    var scale=0;
    var url="";
    //Number of neonatal deaths
    if(data_type=="Health"){
        scale_type = 0;
        normalize_function = 'polinomial';
        $("#title").text("Number of neonatal deaths 2012-2014");
        url ="http://api.worldbank.org/countries/indicators/SH.DTH.NMRT?per_page=3800&date=2012:2014&format=jsonP&prefix=getdata";
    }
    //Lower secondary completion rate, total EDUCATION
    else if(data_type=="Education"){
        normalize_function = 'lineal';
        scale_type = 1;
        url ="http://api.worldbank.org/countries/indicators/SE.SEC.CMPT.LO.ZS?per_page=3000&date=2005:2014&format=jsonP&prefix=getdata";
        $("#title").text("Lower secondary completion raten 2005 - 2014");
    }
    //pobreza per capita $1.25/dia poverty
    else if(data_type=="Poverty"){
        normalize_function = 'logarithmic';
        scale_type = 0;
        url = 'http://api.worldbank.org/countries/indicators/SI.POV.GAPS?per_page=10000&date=2008:2014&format=jsonP&prefix=getdata';
        $("#title").text("World poverty gap $1.25/day 2008 - 2014");
    }

    $('#world-map').empty().html('Loading...');

    $.ajax({
        url : url,
        dataType:"jsonp",
        jsonpCallback:"getdata",
        success: ParseJsonP
    });

}
GetData('Poverty');
