/**
 * Route Optimization API
 * Our Route Optimization API solves the so called vehicle routing problem fast. It calculates an optimal tour for a set of vehicles, services and constraints
 *
 * OpenAPI spec version: 1.0
 * 
 *
 * NOTE: This class is auto generated by the swagger code generator program.
 * https://github.com/swagger-api/swagger-codegen.git
 * Do not edit the class manually.
 */

#ifndef SWGHELPERS_H
#define SWGHELPERS_H

#include <QJsonValue>

namespace Swagger {
    void setValue(void* value, QJsonValue obj, QString type, QString complexType);
    void toJsonArray(QList<void*>* value, QJsonArray* output, QString innerName, QString innerType);
    void toJsonValue(QString name, void* value, QJsonObject* output, QString type);
    bool isCompatibleJsonValue(QString type);
    QString stringValue(QString* value);
    QString stringValue(qint32 value);
    QString stringValue(qint64 value);
    QString stringValue(bool value);
}

#endif // SWGHELPERS_H
