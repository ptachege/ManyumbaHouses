/**
 * Created by nikolay_smeh on 04.01.16.
 * Email: nikolay@nikolay.ws
 * www.nikolay.ws
 */


(function($) {
    var methods = {
        init: function(obj, options) {

            var $this = $(this),
                data = $this.data('daterangeBar');

            if (!data) {
                $(this).data('daterangeBar', {
                    target : obj
                });
            }
            methods.renderBar(obj, options);

            return this;
        },

        renderBar: function(obj, options) {

            var startDateDayArr, startDateTimeArr, startDate, endDateDayArr, endDate, endDateTimeArr;

            var startDateArr = options.startDate.split(' ');
            if (startDateArr[1] != undefined){
                startDateDayArr = startDateArr[0].split('-');
                startDateTimeArr = startDateArr[1].split(':');
                startDate = new Date(startDateDayArr[2], startDateDayArr[1]-1, startDateDayArr[0], startDateTimeArr[0], startDateTimeArr[1], startDateTimeArr[2]);
            }
            else{
                startDateDayArr = startDateArr[0].split('-');
                startDate = new Date(startDateDayArr[2], startDateDayArr[1]-1, startDateDayArr[0]);
            }



            var endDateArr = options.endDate.split(' ');
            if (endDateArr[1] != undefined){
                endDateDayArr = endDateArr[0].split('-');
                endDateTimeArr = endDateArr[1].split(':');
                endDate = new Date(endDateDayArr[2], endDateDayArr[1]-1, endDateDayArr[0], endDateTimeArr[0], endDateTimeArr[1], endDateTimeArr[2]);

            }
            else{
                endDateDayArr = endDateArr[0].split('-');
                endDate = new Date(endDateDayArr[2], endDateDayArr[1]-1, endDateDayArr[0]);
            }

            var today = new Date();

            var fullRange = (startDateArr[1]!= undefined ? Math.round((endDate - startDate) / 1000) : Math.round((endDate - startDate) / (1000 * 60 * 60 * 24)));
            var todayRange = (startDateArr[1]!= undefined ? Math.round((today - startDate) / 1000) : Math.round((today - startDate) / (1000 * 60 * 60 * 24)));

            console.log(fullRange);
            console.log(todayRange);

            var dateDiff = Math.round(todayRange * (parseInt(options.maxValue) - parseInt(options.minValue)) / fullRange);
            if (dateDiff < options.minValue){
                dateDiff = options.minValue;
            }
            if (dateDiff > options.maxValue){
                dateDiff = options.maxValue;
            }

            console.log(dateDiff);

            var progress = $('<div/>')
                .addClass('progress');

            if (options.privateColors){
                progress
                    .css('border', '1px solid ' + options.barColor)
                    .css('background-color', options.bgColor);
            }
            else{
                progress
                    .attr('role', 'progressbar')
                    .attr('aria-valuenow', dateDiff)
                    .attr('aria-valuemin', options.minValue)
                    .attr('aria-valuemax', options.maxValue);
            }

            var progressBar = $('<div/>')
                .addClass('progress-bar')
                .css('width', dateDiff + '%');

            if (options.privateColors){
                progressBar
                    .css('background-color', options.barColor);
            }

            if (options.barClass != undefined){
                progressBar.addClass(options.barClass);
            }
            //progressBar.text(dateDiff + '% ' + options.msg);
			
			var progressText = $('<div/>')
				.css('float', 'left');
			progressText.text(dateDiff + '% ' + options.msg);
            $(progress).append(progressBar);
			$(progress).attr('data-after',dateDiff + '% ' + options.msg);
			//$(progress).append(progressText);
            obj.append(progress);
        }
    };


    $.fn.daterangeBar = function(options) {
        var settings = $.extend({
            'msg': 'of the year',
            'startDate': '01-01-2016',
            'endDate': '31-12-2016',
            'barClass': undefined,
            'bootstrap': false,
            'privateColors': true,
            'barColor': '#7BA7B5',
            'bgColor': '#9CD3E6',
            'minValue': 0,
            'maxValue': 100
        }, options);

        return methods.init(this, settings);
    }
})(jQuery);