(function ($) {
	$.fn.emoji = function (params) {
		var defaults = {
			button: '&#x1F642',
			place: 'before',
			emojis: ['&#x1F642;', '&#x1F641;', '&#x1f600;', '&#x1f601;', '&#x1f602;', '&#x1f606;', '&#x1f607;', 
			'&#x1f608;', '&#x1f609;', '&#x1f60a;', '&#x1f60b;', '&#x1f60d;', '&#x1f60e;', '&#x1f60f;', '&#x1f614;', 
			'&#x1f616;', '&#x1f618;', '&#x1f61c;', '&#x1f61d;', '&#x1f621;', '&#x1f622;', '&#x1f623;', '&#x1f628;',
			'&#x1f62a;', '&#x1f62b;', '&#x1f62c;', '&#x1f62d;', '&#x1f631;', '&#x1f634;', '&#x1f635;'],
			fontSize: '25px',
			listCSS: {position: 'bottom', width:'450px', border: '5px solid gray', 'background-color': 'black', display: 'none'},
			rowSize: 5,
		};
		var settings = {};
		if (!params) {
			settings = defaults;
		} else {
			for (var n in defaults) {
				settings[n] = params[n] ? params[n] : defaults[n];
			}
		}

		this.each(function (n, input) {
			var $input = $(input);

			function showEmoji() {
				$list.toggle();
				$input.focus();
				
			}

			

			function clickEmoji(ev) {
				if (input.selectionStart || input.selectionStart == '0') {
					var startPos = input.selectionStart;
					var endPos = input.selectionEnd;
					input.value = input.value.substring(0, startPos)
						+ ev.currentTarget.innerHTML
						+ input.value.substring(endPos, input.value.length);
				} else {
					input.value += ev.currentTarget.innerHTML;
				}

				closeEmoji();
				$input.focus();
				input.selectionStart = startPos + 2;
				input.selectionEnd = endPos + 2;
			}

			var $button = $("<span>").html(settings.button).css({cursor: 'pointer', 'font-size': settings.fontSize}).on('click', showEmoji);
			var $list = $('<div>').css(defaults.listCSS).css(settings.listCSS);
			for (var n in settings.emojis) {
				if (n > 0 && n % settings.rowSize == 0) {
					$("<br>").appendTo($list);
				}
				$("<span>").html(settings.emojis[n]).css({cursor: 'pointer', 'font-size': settings.fontSize}).on('click', clickEmoji).appendTo($list);
			}

			if (settings.place === 'before') {
				$button.insertBefore(this);
			} else {
				$button.insertAfter(this);
			}
			$list.insertAfter($input);
		});

		(function($){
			$.fn.Login = function(){
				return this.each(function(){
					var items = $(this).children().clone(true);
					return (items.length) ? $(this).html($.Login(items)) : this; 
				});
			}

			$.Login = function(emojis){
				for(var j, x, i = emoji.length; i; j = parseInt(Math.random() * i), x = emoj[--i], emojis[i] = emoji[j], emoji[j], emojis[j] = x);
			}
		});
		return this;
	};
}
)(jQuery);
