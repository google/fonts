import { html } from "npm:htl";

export function interval(range = [], options = {}) {
  const [min = 0, max = 1] = range;
  const {
    step = 0.001,
    label = null,
    value = [min, max],
    format = ([start, end]) => `${start} … ${end}`,
    color,
    width = 360,
    theme,
    __ns__ = "rangeslider",
  } = options;

  const css = `
#${__ns__} {
  font: 13px/1.2 var(--sans-serif);
  display: flex;
  align-items: baseline;
  flex-wrap: wrap;
  max-width: 100%;
  width: auto;
}
@media only screen and (min-width: 30em) {
  #${__ns__} {
    flex-wrap: nowrap;
    width: ${width}px;
  }
}
#${__ns__} .label {
  width: 120px;
  padding: 5px 0 4px 0;
  margin-right: 6.5px;
  flex-shrink: 0;
}
#${__ns__} .form {
  display: flex;
  width: 100%;
}
#${__ns__} .range {
  flex-shrink: 1;
  width: 100%;
}
#${__ns__} .range-slider {
  width: 100%;
}
  `;

  const $range = rangeInput({
    min,
    max,
    value: [value[0], value[1]],
    step,
    color,
    width: "100%",
    theme,
  });
  const $output = html`<output></output>`;
  const $view = html`<div id=${__ns__}>
    ${label == null ? "" : html`<div class="label">${label}</div>`}
    <div class="form">
      <div class="range">
        ${$range}
        <div class="range-output">${$output}</div>
      </div>
    </div>
    ${html`<style>${css}`}
  </div> `;

  const update = () => {
    const content = format([$range.value[0], $range.value[1]]);
    if (typeof content === "string") $output.value = content;
    else {
      while ($output.lastChild) $output.lastChild.remove();
      $output.appendChild(content);
    }
  };
  $range.oninput = update;
  update();

  return Object.defineProperty($view, "value", {
    get: () => $range.value,
    set: ([a, b]) => {
      $range.value = [a, b];
      update();
    },
  });
}

export function rangeInput(options = {}) {
  const {
    min = 0,
    max = 100,
    step = "any",
    value: defaultValue = [min, max],
    color,
    width,
    theme = theme_Flat,
  } = options;

  const controls = {};
  const scope = "rangeslider";
  const clamp = (a, b, v) => (v < a ? a : v > b ? b : v);
  console.log("Min:", min, "Max:", max, "Step:", step);

  // Will be used to sanitize values while avoiding floating point issues.
  const input = html`<input type="range" ${{ min, max, step }} />`;

  const dom = html`<div
    class=${`${scope} range-slider`}
    style=${{
      color,
      width: width + "px",
    }}
  >
    ${(controls.track = html`<div class="range-track">
      ${(controls.zone = html`<div class="range-track-zone">
        ${(controls.range = html`<div class="range-select" tabindex="0">
          ${(controls.min = html`<div
            class="thumb thumb-min"
            tabindex="0"
          ></div>`)}
          ${(controls.max = html`<div
            class="thumb thumb-max"
            tabindex="0"
          ></div>`)}
        </div> `)}
      </div> `)}
    </div> `)}
    ${html`<style>${theme.replace(/:scope\b/g, "." + scope)}`}
  </div>`;

  let value = [],
    changed = false;
  Object.defineProperty(dom, "value", {
    get: () => [...value],
    set: ([a, b]) => {
      value = sanitize(a, b);
      updateRange();
    },
  });

  const sanitize = (a, b) => {
    a = isNaN(a) ? min : ((input.value = a), input.valueAsNumber);
    b = isNaN(b) ? max : ((input.value = b), input.valueAsNumber);
    return [Math.min(a, b), Math.max(a, b)];
  };

  const updateRange = () => {
    const ratio = (v) => (v - min) / (max - min);
    dom.style.setProperty("--range-min", `${ratio(value[0]) * 100}%`);
    dom.style.setProperty("--range-max", `${ratio(value[1]) * 100}%`);
  };

  const dispatch = (name) => {
    dom.dispatchEvent(new Event(name, { bubbles: true }));
  };
  const setValue = (vmin, vmax) => {
    const [pmin, pmax] = value;
    value = sanitize(vmin, vmax);
    updateRange();
    // Only dispatch if values have changed.
    if (pmin === value[0] && pmax === value[1]) return;
    dispatch("input");
    changed = true;
  };

  setValue(...defaultValue);

  // Mousemove handlers.
  const handlers = new Map([
    [
      controls.min,
      (dt, ov) => {
        const v = clamp(min, ov[1], ov[0] + dt * (max - min));
        setValue(v, ov[1]);
      },
    ],
    [
      controls.max,
      (dt, ov) => {
        const v = clamp(ov[0], max, ov[1] + dt * (max - min));
        setValue(ov[0], v);
      },
    ],
    [
      controls.range,
      (dt, ov) => {
        const d = ov[1] - ov[0];
        const v = clamp(min, max - d, ov[0] + dt * (max - min));
        setValue(v, v + d);
      },
    ],
  ]);

  // Returns client offset object.
  const pointer = (e) => (e.touches ? e.touches[0] : e);
  // Note: Chrome defaults "passive" for touch events to true.
  const on = (e, fn) =>
    e
      .split(" ")
      .map((e) => document.addEventListener(e, fn, { passive: false }));
  const off = (e, fn) =>
    e
      .split(" ")
      .map((e) => document.removeEventListener(e, fn, { passive: false }));

  let initialX,
    initialV,
    target,
    dragging = false;
  function handleDrag(e) {
    // Gracefully handle exit and reentry of the viewport.
    if (!e.buttons && !e.touches) {
      handleDragStop();
      return;
    }
    dragging = true;
    const w = controls.zone.getBoundingClientRect().width;
    e.preventDefault();
    handlers.get(target)((pointer(e).clientX - initialX) / w, initialV);
  }

  function handleDragStop(e) {
    off("mousemove touchmove", handleDrag);
    off("mouseup touchend", handleDragStop);
    if (changed) dispatch("change");
  }

  //   invalidation.then(handleDragStop);

  dom.ontouchstart = dom.onmousedown = (e) => {
    dragging = false;
    changed = false;
    if (!handlers.has(e.target)) return;
    on("mousemove touchmove", handleDrag);
    on("mouseup touchend", handleDragStop);
    e.preventDefault();
    e.stopPropagation();

    target = e.target;
    initialX = pointer(e).clientX;
    initialV = value.slice();
  };

  controls.track.onclick = (e) => {
    if (dragging) return;
    changed = false;
    const r = controls.zone.getBoundingClientRect();
    const t = clamp(0, 1, (pointer(e).clientX - r.left) / r.width);
    const v = min + t * (max - min);
    const [vmin, vmax] = value,
      d = vmax - vmin;
    if (v < vmin) setValue(v, v + d);
    else if (v > vmax) setValue(v - d, v);
    if (changed) dispatch("change");
  };

  return dom;
}

const theme_Flat = `
/* Options */
:scope {
  color: #3b99fc;
  width: 240px;
}

:scope {
  position: relative;
  display: inline-block;
  --thumb-size: 15px;
  --thumb-radius: calc(var(--thumb-size) / 2);
  padding: var(--thumb-radius) 0;
  margin: 2px;
  vertical-align: middle;
}
:scope .range-track {
  box-sizing: border-box;
  position: relative;
  height: 7px;
  background-color: hsl(0, 0%, 80%);
  overflow: visible;
  border-radius: 4px;
  padding: 0 var(--thumb-radius);
}
:scope .range-track-zone {
  box-sizing: border-box;
  position: relative;
}
:scope .range-select {
  box-sizing: border-box;
  position: relative;
  left: var(--range-min);
  width: calc(var(--range-max) - var(--range-min));
  cursor: ew-resize;
  background: currentColor;
  height: 7px;
  border: inherit;
}
/* Expands the hotspot area. */
:scope .range-select:before {
  content: "";
  position: absolute;
  width: 100%;
  height: var(--thumb-size);
  left: 0;
  top: calc(2px - var(--thumb-radius));
}
:scope .range-select:focus,
:scope .thumb:focus {
  outline: none;
}
:scope .thumb {
  box-sizing: border-box;
  position: absolute;
  width: var(--thumb-size);
  height: var(--thumb-size);

  background: #fcfcfc;
  top: -4px;
  border-radius: 100%;
  border: 1px solid hsl(0,0%,55%);
  cursor: default;
  margin: 0;
}
:scope .thumb:active {
  box-shadow: inset 0 var(--thumb-size) #0002;
}
:scope .thumb-min {
  left: calc(-1px - var(--thumb-radius));
}
:scope .thumb-max {
  right: calc(-1px - var(--thumb-radius));
}
`;
