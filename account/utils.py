from collections import OrderedDict

def chart_config(caption, xAxisName=None, yAxisName=None, theme="fusion"):
    """
        Configurations for each chart.

        args:
            caption: The caption to be displayed in the chart
            xAxisName (opt): The label to be assigned to the x axis
            yAxisName (opt): The label to be assigned to the y axis
        
        return:
            OrderedDict containing the arguments passed in
    
    """

    # The `chartConfig` dict contains key-value pairs of data for chart attribute
    chartConfig = OrderedDict()
    chartConfig["caption"] = caption
    chartConfig["theme"] = "fusion"
    
    if xAxisName and yAxisName:
        chartConfig["xAxisName"] = xAxisName
        chartConfig["yAxisName"] = yAxisName

    return chartConfig


def map_data_to_dict(chartData, chartConfig):
    """
        Map chart data to dictionary.

        args:
            chartData: dictionary of data you want to plot.
            chartConfig: dictionary of chart meta data such as xAxisName, yAxisName, etc
    """

    # Chart data is passed to the `dataSource` parameter, like a dictionary in the form of key-value pairs.
    dataSource = OrderedDict()

    chartData = OrderedDict(chartData)
    

    dataSource["chart"] = chartConfig
    dataSource["data"] = []

    # Convert the data in the `chartData`array into a format that can be consumed by FusionCharts.
    #The data for the chart should be in an array wherein each element of the array
    #is a JSON object# having the `label` and `value` as keys.

    #Iterate through the data in `chartData` and insert into the `dataSource['data']` list.
    for key, value in chartData.items():
        data = {}
        data["label"] = key
        data["value"] = value
        dataSource["data"].append(data)
    
    return dataSource