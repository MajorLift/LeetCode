// https://leetcode.com/problems/event-emitter

type Callback = (...args: any[]) => any;
type Subscription = {
    unsubscribe: () => void
}

class EventEmitter {
  callbacks = {}

  subscribe(eventName: string, callback: Callback): Subscription {
    this.callbacks[eventName] = [...(this.callbacks[eventName] ?? []), callback]
    return {
      unsubscribe: () => {
        this.callbacks[eventName] = this.callbacks[eventName].filter((e) => e !== callback)
      }
    };
  }

  emit(eventName: string, args: any[] = []): any {
    return this.callbacks[eventName]?.map((cb) => cb(...args)) ?? []
  }
}

/**
 * const emitter = new EventEmitter();
 *
 * // Subscribe to the onClick event with onClickCallback
 * function onClickCallback() { return 99 }
 * const sub = emitter.subscribe('onClick', onClickCallback);
 *
 * emitter.emit('onClick'); // [99]
 * sub.unsubscribe(); // undefined
 * emitter.emit('onClick'); // []
 */