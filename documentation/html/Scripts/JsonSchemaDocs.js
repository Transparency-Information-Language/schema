if (typeof jQuery === 'undefined') {
    throw new Error('Bootstrap\'s JavaScript requires jQuery')
}

// Formats json text adding divs to syntax highlight it.
function syntaxHighlight(json) {
    if (typeof json != 'string') {
        json = JSON.stringify(json, undefined, 4);
    }
    json = json.replace(/&/g, '&amp;').replace(/</g, '&lt;').replace(/>/g, '&gt;');
    return json.replace(/("(\\u[a-zA-Z0-9]{4}|\\[^u]|[^\\"])*"(\s*:)?|\b(true|false|null)\b|-?\d+(?:\.\d*)?(?:[eE][+\-]?\d+)?)/g, function (match) {
        var cls = 'number';
        if (/^"/.test(match)) {
            if (/:$/.test(match)) {
                cls = 'key';
            } else {
                cls = 'string';
            }
        } else if (/true|false/.test(match)) {
            cls = 'boolean';
        } else if (/null/.test(match)) {
            cls = 'null';
        }
        return '<span class="' + cls + '">' + match + '</span>';
    });
}

function ensureInFrame(itemType, selectedItemType) {
    if (window.name != 'ContentFrame') {
        /* if were not open in a frame - load the frame */
        var url = document.location;
        if (url.length > 0 && url[0] == '/')
            url = url.substring(1, url.length);

        document.location = 'index.html?url=' + url;
    }
    else {
        $(function () {
            //set initial state of the collapsable sections
            setState('.expand');

            $('.expand').click(function () {
                expandContract(this);
            });

            if ($.urlParam('sync') == '') {
                if (window.parent.frames["MenuFrame"] != null && itemType != null && selectedItemType != null) {
                    window.parent.frames["MenuFrame"].selectItem(itemType, selectedItemType);
                }
            }
        });
    }
}

function getURLParam(strParamName) 
{
    var strReturn = "";
    var strHref = window.location.href;
    if (strHref.indexOf("?") > -1) 
    {
        var strQueryString = strHref.substr(strHref.indexOf("?")).toLowerCase();
        var aQueryString = strQueryString.split("&");
        for (var iParam = 0; iParam < aQueryString.length; iParam++) 
        {
            if (aQueryString[iParam].indexOf(strParamName.toLowerCase() + "=") > -1) 
            {
                var aParam = aQueryString[iParam].split("=");
                strReturn = aParam[1];
                break;
            }
        }
    }
    return unescape(strReturn);
}

$(function () {
    // Attach handlers to deal with expand/collapse of collapsible regions
    $('.clickable').on("click", function (e) {
        if ($(this).hasClass('panel-collapsed')) {
            // expand the panel
            $(this).parents('.collapsable-row').find('.collapsable-row-body').slideDown();
            $(this).removeClass('panel-collapsed');
            $(this).find('i').removeClass('glyphicon-chevron-down').addClass('glyphicon-chevron-up');
        }
        else {
            // collapse the panel
            $(this).parents('.collapsable-row').find('.collapsable-row-body').slideUp();
            $(this).addClass('panel-collapsed');
            $(this).find('i').removeClass('glyphicon-chevron-up').addClass('glyphicon-chevron-down');
        }
    });

    // Reformats and color code the json code
    $("pre.json").each(function () {
        $(this).html(syntaxHighlight($(this).text()));
    });
});

