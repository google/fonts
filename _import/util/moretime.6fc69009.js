import { timeInterval } from "../../_node/d3-time@3.1.1/index.03ee5af2.js";

export const utcQuarter = timeInterval(
  (date) => {
    date.setUTCDate(1);
    date.setUTCHours(0, 0, 0, 0);
  },
  (date, step) => {
    date.setUTCMonth(date.getUTCMonth() + 3 * step);
  },
  (start, end) => {
    return (
      (end.getUTCMonth() -
        start.getUTCMonth() +
        (end.getUTCFullYear() - start.getUTCFullYear()) * 12) /
      3
    );
  },
  (date) => {
    return date.getUTCMonth() / 3;
  }
);
