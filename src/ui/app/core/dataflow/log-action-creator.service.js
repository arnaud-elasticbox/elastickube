/*
Copyright 2016 ElasticBox All rights reserved.

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

    http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
*/

class LogActionCreatorService {

    constructor($q, actions, dispatcher, logsAPI) {
        'ngInject';

        this._$q = $q;
        this._actions = actions;
        this._logsAPI = logsAPI;
        this._dispatcher = dispatcher;
    }

    loadLogs(namespace, name, container, tailLines) {
        const loadBody = {
            namespace,
            name,
            container,
            tailLines
        };

        this._dispatcher.dispatch({ type: this._actions.LOGS_LOAD });
        return this._logsAPI.load(loadBody)
            .then((logs) => {
                this._dispatcher.dispatch({ type: this._actions.LOGS_LOADED, namespace, name, container, logs });
            });
    }
}

export default LogActionCreatorService;
