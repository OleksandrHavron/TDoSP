'use strict';
const slider = () => {

    const slider = document.getElementById('app_slider');
    const slider_wrapper = document.getElementById('app_wrapper');
    const slider_items = document.querySelectorAll('[data-app_item]');
    let clicked = false;
    let positioner = 0;
    let prev_value, prev_val_IE;
    let prev_time = 0, current_time = 0;

    const slider_width = () => {
        return parseFloat(getComputedStyle(slider).width);
    }

    const slides_line_width = () => {
        let accumulator = 0;

        if (!/MSIE \d|Trident.*rv:/.test(navigator.userAgent)) {// for IE
            for (let i = 0; i < slider_items.length; i++) {
                accumulator += parseFloat(getComputedStyle(slider_items[i]).width);
            }
        } else {
            for (let i = 0; i < slider_items.length; i++) {
                accumulator += slider_items[i].offsetWidth;
            }
        }
        return accumulator;
    }

    const checker_and_changer = (positioner, result) => {
        if (positioner < -(slides_line_width() - slider_width())) {
            positioner -= result;
        }
        if (positioner > 0) {
            positioner -= result;
        }
        return positioner;
    }

    const mouse_action = (event) => {
        if (clicked) {
            if (/MSIE \d|Trident.*rv:/.test(navigator.userAgent)) {// for IE
                let curr_val_IE = event.pageX;
                let result = curr_val_IE - prev_val_IE;
                prev_val_IE = curr_val_IE;
                positioner += result;
                positioner = checker_and_changer(positioner, result);
                slider_wrapper.style.left = `${positioner}px`;
            } else {
                let move_ind = event.movementX;
                positioner += move_ind;
                positioner = checker_and_changer(positioner, move_ind);
                slider_wrapper.style.left = `${positioner}px`;
            }
        }
    }

    const touch_freeze = (event) => {
        const currentTouch = event.touches[0];
        prev_value = currentTouch;
    }
    const touch_action = (event) => {
        if (clicked) {
            const currentTouch = event.touches[0];
            let res = currentTouch.pageX - prev_value.pageX;
            prev_value = currentTouch;
            positioner += res;
            positioner = checker_and_changer(positioner, res);
            slider_wrapper.style.left = `${positioner}px`;
        }
    }
    const judge = (bool = false) => {
        return bool;
    }
    const permit = () => {
        let res
        if (prev_time !== 0 && current_time !== 0) {
            res = current_time - prev_time;
        }
        return res < 100;
    }
    const linker = (event) => {
        if (event.target.src) {
            let defaultLocation = event.target.parentNode.href;
            event.preventDefault();
            if (permit()) {
                location.href = defaultLocation;
            }
        }
    }

    const main = () => {
        slider_wrapper.addEventListener('dragstart', (event) => {
            event.preventDefault();
        }, false)
        slider_wrapper.addEventListener('mousedown', (event) => {
            clicked = judge(true);
            prev_val_IE = event.pageX;
            let time = new Date();
            prev_time = time.getTime();
        }, false);
        slider_wrapper.addEventListener('mouseleave', () => {
            clicked = judge(false);
        }, false);
        slider_wrapper.addEventListener('mouseup', () => {
            clicked = judge(false);
            let time = new Date();
            current_time = time.getTime();
        }, false);
        slider_wrapper.addEventListener('touchmove', () => {
            clicked = judge(true);
        }, false);
        slider_wrapper.addEventListener('mousemove', mouse_action, false);
        slider_wrapper.addEventListener('touchstart', touch_freeze, false);
        slider_wrapper.addEventListener('touchmove', touch_action, false);
        // console.log(location);
        slider_items.forEach((elem) => {
            elem.addEventListener('click', linker, false);
        })
    }
    main();
}
slider();
